"""
Evaluation of NURBS objects in Python (implemented in Rust)
"""
from typing import Iterable, List


def bernstein_poly(n: int, i: int, t: float) -> float:
    r"""
    Evaluates the Bernstein polynomial at a single :math:`t`-value. The Bernstein polynomial is given by

    .. math::

        B_{i,n}(t)={n \choose i} t^i (1-t)^{n-i}

    Parameters
    ----------
    n: int
        Degree of the polynomial
    i: int
        Index
    t: float
        Parameter value :math:`t` at which to evaluate
    
    Returns
    -------
    float
        Value of the Bernstein polynomial at :math:`t`
    """

def bezier_curve_eval(p: Iterable[Iterable[float]], t: float) -> List[float]:
    r"""
    Evaluates a Bézier curve with :math:`n+1` control points at a single :math:`t`-value according to

    .. math::

        \mathbf{C}(t) = \sum\limits_{i=0}^n B_{i,n}(t) \mathbf{P}_i

    where :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    t: float
        Parameter value :math:`t` at which to evaluate
    
    Returns
    -------
    List[float]
        Value of the Bézier curve at :math:`t`. Has the same size as the inner dimension of ``p``
    """

def bezier_curve_eval_dp(i: int, n: int, dim: int, t: float) -> List[float]:
    r"""
    Evaluates the derivative of the Bézier curve with respect to an individual control point at a given :math:`t`-value
    
    Parameters
    ----------
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: float
        Parameter value at which to evaluate the curve sensitivity
    
    Returns
    -------
    List[float]
        1-D list representing the curve sensitivity at :math:`t` to the control point :math:`\mathbf{P}_i`
    """

def bezier_curve_dcdt(p: Iterable[Iterable[float]], t: float) -> List[float]:
    r"""
    Evaluates the first derivative (with respect to :math:`t`) of a Bézier curve with :math:`n+1` control 
    points at a single :math:`t`-value according to

    .. math::

        \frac{\text{d}}{\text{d}t} \mathbf{C}(t) = \sum\limits_{i=0}^{n-1} B_{i,n-1}(t) \left[n\left( \mathbf{P}_{i+1} - \mathbf{P}_i \right)\right]

    where :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    t: float
        Parameter value :math:`t` at which to evaluate
    
    Returns
    -------
    List[float]
        Value of the Bézier curve first derivative at :math:`t`. Has the same size as the inner dimension of ``p``
    """

def bezier_curve_dcdt_dp(i: int, n: int, dim: int, t: float) -> List[float]:
    r"""
    Evaluates the derivative of the Bézier curve first derivative with respect to an individual control point
  
    Parameters
    ----------
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: float
        Parameter value at which to evaluate the curve derivative sensitivity
    
    Returns
    -------
    List[float]
        1-D list representing the curve derivative sensitivity at :math:`t` to the control point :math:`\mathbf{P}_i`
    """

def bezier_curve_d2cdt2(p: Iterable[Iterable[float]], t: float) -> List[float]:
    r"""
    Evaluates the second derivative (with respect to :math:`t`) of a Bézier curve with :math:`n+1` control 
    points at a single :math:`t`-value according to

    .. math::

        \frac{\text{d}^2}{\text{d}t^2} \mathbf{C}(t) = \sum\limits_{i=0}^{n-2} B_{i,n-2}(t) \left[n(n-1)\left(\mathbf{P}_{i+2} - 2 \mathbf{P}_{i+1} + \mathbf{P}_i \right)\right]

    where :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    t: float
        Parameter value :math:`t` at which to evaluate
    
    Returns
    -------
    List[float]
        Value of the Bézier curve first derivative at :math:`t`. Has the same size as the inner dimension of ``p``
    """

def bezier_curve_d2cdt2_dp(i: int, n: int, dim: int, t: float) -> List[float]:
    r"""
    Evaluates the derivative of the Bézier curve second derivative with respect to an individual control point
  
    Parameters
    ----------
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: float
        Parameter value at which to evaluate the curve derivative sensitivity
    
    Returns
    -------
    List[float]
        1-D list representing the curve derivative sensitivity at :math:`t` to the control point :math:`\mathbf{P}_i`
    """

def bezier_curve_eval_grid(p: Iterable[Iterable[float]], nt: int) -> List[List[float]]:
    r"""
    Evaluates a Bézier curve with :math:`n+1` control points at :math:`N_t` linearly-spaced points according to

    .. math::

        \mathbf{C}(t) = \sum\limits_{i=0}^n B_{i,n}(t) \mathbf{P}_i

    where :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.
    
    Returns
    -------
    List[List[float]]
        Value of the Bézier curve at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def bezier_curve_eval_dp_grid(i: int, n: int, dim: int, nt: int) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a Bézier curve with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the control point sensitivity of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the Bézier curve control point sensitivity at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def bezier_curve_dcdt_grid(p: Iterable[Iterable[float]], nt: int) -> List[List[float]]:
    r"""
    Evaluates the first derivative (with respect to :math:`t`) of a Bézier curve with :math:`n+1` control 
    points at :math:`N_t` linearly-spaced points according to

    .. math::

        \frac{\text{d}}{\text{d}t} \mathbf{C}(t) = \sum\limits_{i=0}^{n-1} B_{i,n-1}(t) \left[n\left( \mathbf{P}_{i+1} - \mathbf{P}_i \right)\right]

    where :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.
    
    Returns
    -------
    List[List[float]]
        Value of the Bézier curve first derivative at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def bezier_curve_dcdt_dp_grid(i: int, n: int, dim: int, nt: int) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a Bézier curve first derivative with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the control point sensitivity of the curve first derivative at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the Bézier curve first derivative control point sensitivity at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def bezier_curve_d2cdt2_grid(p: Iterable[Iterable[float]], nt: int) -> List[List[float]]:
    r"""
    Evaluates the second derivative (with respect to :math:`t`) of a Bézier curve with :math:`n+1` control 
    points at :math:`N_t` linearly-spaced points according to

    .. math::

        \frac{\text{d}^2}{\text{d}t^2} \mathbf{C}(t) = \sum\limits_{i=0}^{n-2} B_{i,n-2}(t) \left[n(n-1)\left(\mathbf{P}_{i+2} - 2 \mathbf{P}_{i+1} + \mathbf{P}_i \right)\right]

    where :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the Bézier curve first derivative at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def bezier_curve_d2cdt2_dp_grid(i: int, n: int, dim: int, nt: int) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a Bézier curve second derivative with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the control point sensitivity of the curve second derivative at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the Bézier curve second derivative control point sensitivity at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def bezier_curve_eval_tvec(p: Iterable[Iterable[float]], t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates a Bézier curve with :math:`n+1` control points along a vector of :math:`t`-values according to

    .. math::

        \mathbf{C}(t) = \sum\limits_{i=0}^n B_{i,n}(t) \mathbf{P}_i

    where :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    t: Iterable[float]
        Parameter vector along which to evaluate the curve
    
    Returns
    -------
    List[List[float]]
        Value of the Bézier curve along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def bezier_curve_eval_dp_tvec(i: int, n: int, dim: int, t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a Bézier curve with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: Iterable[float]
        Parameter vector along which to evaluate the curve control point sensitivity

    Returns
    -------
    List[List[float]]
        Value of the Bézier curve control point sensitivity along parameter vector :math:`\mathbf{t}`. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def bezier_curve_dcdt_tvec(p: Iterable[Iterable[float]], t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates the first derivative (with respect to :math:`t`) of a Bézier curve with :math:`n+1` control 
    points along a vector of :math:`t`-values according to

    .. math::

        \frac{\text{d}}{\text{d}t} \mathbf{C}(t) = \sum\limits_{i=0}^{n-1} B_{i,n-1}(t) \left[n\left( \mathbf{P}_{i+1} - \mathbf{P}_i \right)\right]

    where :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    t: Iterable[float]
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.
    
    Returns
    -------
    List[List[float]]
        Value of the Bézier curve first derivative along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def bezier_curve_dcdt_dp_tvec(i: int, n: int, dim: int, t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a Bézier curve first derivative with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: Iterable[float]
        Parameter vector along which to evaluate the curve first derivative control point sensitivity

    Returns
    -------
    List[List[float]]
        Value of the Bézier curve first derivative control point sensitivity along parameter vector :math:`\mathbf{t}`. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def bezier_curve_d2cdt2_tvec(p: Iterable[Iterable[float]], t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates the second derivative (with respect to :math:`t`) of a Bézier curve with :math:`n+1` control 
    points along a vector of :math:`t`-values according to

    .. math::

        \frac{\text{d}^2}{\text{d}t^2} \mathbf{C}(t) = \sum\limits_{i=0}^{n-2} B_{i,n-2}(t) \left[n(n-1)\left(\mathbf{P}_{i+2} - 2 \mathbf{P}_{i+1} + \mathbf{P}_i \right)\right]

    where :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    t: Iterable[float]
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the Bézier curve first derivative along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def bezier_curve_d2cdt2_dp_tvec(i: int, n: int, dim: int, t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a Bézier curve second derivative with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: Iterable[float]
        Parameter vector along which to evaluate the curve second derivative control point sensitivity

    Returns
    -------
    List[List[float]]
        Value of the Bézier curve second derivative control point sensitivity along parameter vector :math:`\mathbf{t}`. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def bezier_surf_eval(p: Iterable[Iterable[Iterable[float]]], u: float, v: float) -> List[float]:
    r"""
    Evaluates a Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair according to

    .. math::

        \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m B_{i,n}(u) B_{j,m}(v) \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface
    
    Returns
    -------
    List[float]
        Value of the Bézier surface at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def bezier_surf_dsdu(p: Iterable[Iterable[Iterable[float]]], u: float, v: float) -> List[float]:
    r"""
    Evaluates the first derivative with respect to :math:`u` of a Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction and :math:`m+1` control points in the 
    :math:`v`-direction at a :math:`(u,v)` parameter pair according to

    .. math::

        \frac{\text{d}}{\text{d}u} \mathbf{S}(u,v) = n \sum\limits_{i=0}^n \sum\limits_{j=0}^m \left[ B_{i - 1,n - 1}(u) - B_{i,n - 1}(u) \right] B_{j,m}(v) \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the Bézier surface first derivative with respect to :math:`u` at :math:`(u,v)`. Has the same size as the 
        innermost dimension of ``p``
    """

def bezier_surf_dsdv(p: Iterable[Iterable[Iterable[float]]], u: float, v: float) -> List[float]:
    r"""
    Evaluates the first derivative with respect to :math:`v` of a Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction and :math:`m+1` control points in the 
    :math:`v`-direction at a :math:`(u,v)` parameter pair according to

    .. math::

        \frac{\text{d}}{\text{d}v} \mathbf{S}(u,v) = m \sum\limits_{i=0}^n \sum\limits_{j=0}^m B_{i,n}(u) \left[ B_{j - 1,m - 1}(v) - B_{j,m - 1}(v) \right] \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the Bézier surface first derivative with respect to :math:`v` at :math:`(u,v)`. Has the same size as the 
        innermost dimension of ``p``
    """

def bezier_surf_d2sdu2(p: Iterable[Iterable[Iterable[float]]], u: float, v: float) -> List[float]:
    r"""
    Evaluates the second derivative with respect to :math:`u` of a Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction and :math:`m+1` control points in the 
    :math:`v`-direction at a :math:`(u,v)` parameter pair according to

    .. math::

        \frac{\text{d}^2}{\text{d}u^2} \mathbf{S}(u,v) = n(n-1) \sum\limits_{i=0}^n \sum\limits_{j=0}^m \left[ B_{i - 2,n - 2}(u) - 2B_{i - 1,n - 2}(u) + B_{i,n - 2}(u) \right] B_{j,m}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the Bézier surface second derivative with respect to :math:`u` at :math:`(u,v)`. Has the same size as the 
        innermost dimension of ``p``
    """

def bezier_surf_d2sdv2(p: Iterable[Iterable[Iterable[float]]], u: float, v: float) -> List[float]:
    r"""
    Evaluates the first derivative with respect to :math:`v` of a Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction and :math:`m+1` control points in the 
    :math:`v`-direction at a :math:`(u,v)` parameter pair according to

    .. math::

        \frac{\text{d}^2}{\text{d}v^2} \mathbf{S}(u,v) = m(m - 1) \sum\limits_{i=0}^n \sum\limits_{j=0}^m B_{i,n}(u) \left[ B_{j - 2,m - 2}(v) - 2B_{j - 1,m - 2}(v) - B_{j,m - 2}(v) \right] \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the Bézier surface second derivative with respect to :math:`v` at :math:`(u,v)`. Has the same size as the 
        innermost dimension of ``p``
    """

def bezier_surf_eval_dp(i: int, j: int, n: int, m: int, dim: int, u: float, v: float) -> List[float]:
    r"""
    Evaluates the derivative of the Bézier surface with respect to an individual control point at a given :math:`(u,v)`-pair:

    .. math::

        \frac{\partial}{\partial \mathbf{P}_{i,j}} \mathbf{S}(u,v) = B_{i,n}(u) B_{j,m}(v)
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[float]
        1-D list representing the surface sensitivity at :math:`(u,v)` to the control point :math:`\mathbf{P}_{i,j}`
    """

def bezier_surf_dsdu_dp(i: int, j: int, n: int, m: int, dim: int, u: float, v: float) -> List[float]:
    r"""
    Evaluates the derivative of the Bézier surface first :math:`u`-derivative with respect to an individual control point at a given :math:`(u,v)`-pair:

    .. math::

        \frac{\partial}{\partial \mathbf{P}_{i,j}} \left(\partial \frac{\mathbf{S}(u,v)}{\partial u} \right) = n \left[ B_{i - 1,n - 1}(u) - B_{i,n - 1}(u) \right] B_{j,m}(v)
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[float]
        1-D list representing the surface derivative sensitivity at :math:`(u,v)` to the control point :math:`\mathbf{P}_{i,j}`
    """

def bezier_surf_dsdv_dp(i: int, j: int, n: int, m: int, dim: int, u: float, v: float) -> List[float]:
    r"""
    Evaluates the derivative of the Bézier surface first :math:`v`-derivative with respect to an individual control point at a given :math:`(u,v)`-pair:

    .. math::

        \frac{\partial}{\partial \mathbf{P}_{i,j}} \left(\partial \frac{\mathbf{S}(u,v)}{\partial v} \right) = m B_{i,n}(u) \left[ B_{j - 1,m - 1}(v) - B_{j,m - 1}(v) \right]

    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[float]
        1-D list representing the surface derivative sensitivity at :math:`(u,v)` to the control point :math:`\mathbf{P}_{i,j}`
    """

def bezier_surf_d2sdu2_dp(i: int, j: int, n: int, m: int, dim: int, u: float, v: float) -> List[float]:
    r"""
    Evaluates the derivative of the Bézier surface second :math:`u`-derivative with respect to an individual control point at a given :math:`(u,v)`-pair:

    .. math::

        \frac{\partial}{\partial \mathbf{P}_{i,j}} \left(\partial^2 \frac{\mathbf{S}(u,v)}{\partial u^2} \right) = n (n-1) \left[ B_{i - 2,n - 2}(u) - 2B_{i - 1,n - 2}(u) + B_{i,n - 2}(u) \right] B_{j,m}(v)
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[float]
        1-D list representing the surface derivative sensitivity at :math:`(u,v)` to the control point :math:`\mathbf{P}_{i,j}`
    """

def bezier_surf_d2sdv2_dp(i: int, j: int, n: int, m: int, dim: int, u: float, v: float) -> List[float]:
    r"""
    Evaluates the derivative of the Bézier surface second :math:`v`-derivative with respect to an individual control point at a given :math:`(u,v)`-pair:

    .. math::

        \frac{\partial}{\partial \mathbf{P}_{i,j}} \left(\partial^2 \frac{\mathbf{S}(u,v)}{\partial v^2} \right) = m (m-1) B_{i,n}(u) \left[ B_{j - 2,m - 2}(v) - 2B_{j - 1,m - 2}(v) - B_{j,m - 2}(v) \right]

    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[float]
        1-D list representing the surface derivative sensitivity at :math:`(u,v)` to the control point :math:`\mathbf{P}_{i,j}`
    """

def bezier_surf_eval_dp_iso_u(i: int, j: int, n: int, m: int, dim: int, u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the derivative of the Bézier surface with respect to an individual control point along a :math:`u`-isoparametric curve
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface sensitiviies
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def bezier_surf_eval_dp_iso_v(i: int, j: int, n: int, m: int, dim: int, nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the derivative of the Bézier surface with respect to an individual control point along a :math:`v`-isoparametric curve
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface sensitivities
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_u \times d`, where :math:`d` is the number of spatial dimensions
    """

def bezier_surf_dsdu_dp_iso_u(i: int, j: int, n: int, m: int, dim: int, u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the derivative of the Bézier surface first :math:`u`-derivative with respect to an individual control point along a :math:`u`-isoparametric curve
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface sensitiviies
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def bezier_surf_dsdu_dp_iso_v(i: int, j: int, n: int, m: int, dim: int, nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the derivative of the Bézier surface first :math:`u`-derivative with respect to an individual control point along a :math:`v`-isoparametric curve
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface sensitivities
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_u \times d`, where :math:`d` is the number of spatial dimensions
    """

def bezier_surf_dsdv_dp_iso_u(i: int, j: int, n: int, m: int, dim: int, u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the derivative of the Bézier surface first :math:`v`-derivative with respect to an individual control point along a :math:`u`-isoparametric curve
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface sensitiviies
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def bezier_surf_dsdv_dp_iso_v(i: int, j: int, n: int, m: int, dim: int, nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the derivative of the Bézier surface first :math:`v`-derivative with respect to an individual control point along a :math:`v`-isoparametric curve
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface sensitivities
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_u \times d`, where :math:`d` is the number of spatial dimensions
    """

def bezier_surf_d2sdu2_dp_iso_u(i: int, j: int, n: int, m: int, dim: int, u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the derivative of the Bézier surface second :math:`u`-derivative with respect to an individual control point along a :math:`u`-isoparametric curve
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface sensitiviies
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def bezier_surf_d2sdu2_dp_iso_v(i: int, j: int, n: int, m: int, dim: int, nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the derivative of the Bézier surface second :math:`u`-derivative with respect to an individual control point along a :math:`v`-isoparametric curve
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface sensitivities
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_u \times d`, where :math:`d` is the number of spatial dimensions
    """

def bezier_surf_d2sdv2_dp_iso_u(i: int, j: int, n: int, m: int, dim: int, u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the derivative of the Bézier surface second :math:`v`-derivative with respect to an individual control point along a :math:`u`-isoparametric curve
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface sensitiviies
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def bezier_surf_d2sdv2_dp_iso_v(i: int, j: int, n: int, m: int, dim: int, nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the derivative of the Bézier surface second :math:`v`-derivative with respect to an individual control point along a :math:`v`-isoparametric curve
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface sensitivities
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_u \times d`, where :math:`d` is the number of spatial dimensions
    """

def bezier_surf_eval_dp_grid(i: int, j: int, n: int, m: int, dim: int, nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the derivative of the Bézier surface with respect to an individual control point on a :math:`(u,v)` grid
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface sensitiviies
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface sensitiviies

    Returns
    -------
    List[List[List[float]]]
        3-D array of size :math:`N_u \times N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def bezier_surf_dsdu_dp_grid(i: int, j: int, n: int, m: int, dim: int, nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the derivative of the Bézier surface first :math:`u`-derivative with respect to an individual control point on a :math:`(u,v)` grid
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface derivative sensitiviies
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface derivative sensitiviies

    Returns
    -------
    List[List[List[float]]]
        3-D array of size :math:`N_u \times N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def bezier_surf_dsdv_dp_grid(i: int, j: int, n: int, m: int, dim: int, nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the derivative of the Bézier surface first :math:`v`-derivative with respect to an individual control point on a :math:`(u,v)` grid
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface derivative sensitiviies
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface derivative sensitiviies

    Returns
    -------
    List[List[List[float]]]
        3-D array of size :math:`N_u \times N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def bezier_surf_d2sdu2_dp_grid(i: int, j: int, n: int, m: int, dim: int, nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the derivative of the Bézier surface second :math:`u`-derivative with respect to an individual control point on a :math:`(u,v)` grid
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface derivative sensitiviies
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface derivative sensitiviies

    Returns
    -------
    List[List[List[float]]]
        3-D array of size :math:`N_u \times N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def bezier_surf_d2sdv2_dp_grid(i: int, j: int, n: int, m: int, dim: int, nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the derivative of the Bézier surface second :math:`v`-derivative with respect to an individual control point on a :math:`(u,v)` grid
    
    Parameters
    ----------
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface derivative sensitiviies
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface derivative sensitiviies

    Returns
    -------
    List[List[List[float]]]
        3-D array of size :math:`N_u \times N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def bezier_surf_eval_iso_u(p: Iterable[Iterable[Iterable[float]]], u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates an isoparametric curve in :math:`u` of a Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction according to

    .. math::

        \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m B_{i,n}(u) B_{j,m}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` points along the :math:`u`-isoparametric curve of the Bézier surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bezier_surf_eval_iso_v(p: Iterable[Iterable[Iterable[float]]], nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates an isoparametric curve in :math:`v` of a Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u` linearly-spaced points 
    along the :math:`u`-direction according to

    .. math::

        \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m B_{i,n}(u) B_{j,m}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` points along the :math:`v`-isoparametric curve of the Bézier surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bezier_surf_dsdu_iso_u(p: Iterable[Iterable[Iterable[float]]], u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the first derivative w.r.t. :math:`u` along an isoparametric curve in :math:`u` of a 
    Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction according to

    .. math::

        \frac{\text{d}}{\text{d}u} \mathbf{S}(u,v) = n \sum\limits_{i=0}^n \sum\limits_{j=0}^m \left[ B_{i - 1,n - 1}(u) - B_{i,n - 1}(u) \right] B_{j,m}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` first derivatives w.r.t. :math:`u` along the :math:`u`-isoparametric curve of the Bézier surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bezier_surf_dsdu_iso_v(p: Iterable[Iterable[Iterable[float]]], nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the first derivative w.r.t. :math:`u` along an isoparametric curve in :math:`v` of a 
    Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u` linearly-spaced points 
    along the :math:`u`-direction according to

    .. math::

        \frac{\text{d}}{\text{d}u} \mathbf{S}(u,v) = n \sum\limits_{i=0}^n \sum\limits_{j=0}^m \left[ B_{i - 1,n - 1}(u) - B_{i,n - 1}(u) \right] B_{j,m}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` first derivatives w.r.t. :math:`u` along the :math:`v`-isoparametric curve of the Bézier surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bezier_surf_dsdv_iso_u(p: Iterable[Iterable[Iterable[float]]], u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`v` along an isoparametric curve in :math:`u` of a 
    Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction according to

    .. math::

        \frac{\text{d}}{\text{d}v} \mathbf{S}(u,v) = m \sum\limits_{i=0}^n \sum\limits_{j=0}^m B_{i,n}(u) \left[ B_{j - 1,m - 1}(v) - B_{j,m - 1}(v) \right] \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` first derivatives w.r.t. :math:`v` along the :math:`u`-isoparametric curve of the Bézier surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bezier_surf_dsdv_iso_v(p: Iterable[Iterable[Iterable[float]]], nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the first derivative w.r.t. :math:`u` along an isoparametric curve in :math:`v` of a 
    Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u` linearly-spaced points 
    along the :math:`u`-direction according to

    .. math::

        \frac{\text{d}}{\text{d}v} \mathbf{S}(u,v) = m \sum\limits_{i=0}^n \sum\limits_{j=0}^m B_{i,n}(u) \left[ B_{j - 1,m - 1}(v) - B_{j,m - 1}(v) \right] \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` first derivatives w.r.t. :math:`u` along the :math:`v`-isoparametric curve of the Bézier surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bezier_surf_d2sdu2_iso_u(p: Iterable[Iterable[Iterable[float]]], u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`u` along an isoparametric curve in :math:`u` of a 
    Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction according to

    .. math::

        \frac{\text{d}^2}{\text{d}u^2} \mathbf{S}(u,v) = n(n-1) \sum\limits_{i=0}^n \sum\limits_{j=0}^m \left[ B_{i - 2,n - 2} - 2B_{i - 1,n - 2}(u) + B_{i,n - 2}(u) \right] B_{j,m}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` second derivatives w.r.t. :math:`u` along the :math:`u`-isoparametric curve of the Bézier surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bezier_surf_d2sdu2_iso_v(p: Iterable[Iterable[Iterable[float]]], nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`u` along an isoparametric curve in :math:`v` of a 
    Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u` linearly-spaced points 
    along the :math:`u`-direction according to

    .. math::

        \frac{\text{d}^2}{\text{d}u^2} \mathbf{S}(u,v) = n(n-1) \sum\limits_{i=0}^n \sum\limits_{j=0}^m \left[ B_{i - 2,n - 2} - 2B_{i - 1,n - 2}(u) + B_{i,n - 2}(u) \right] B_{j,m}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` second derivatives w.r.t. :math:`u` along the :math:`v`-isoparametric curve of the Bézier surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bezier_surf_d2sdv2_iso_u(p: Iterable[Iterable[Iterable[float]]], u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`v` along an isoparametric curve in :math:`u` of a 
    Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction according to

    .. math::

        \frac{\text{d}^2}{\text{d}v^2} \mathbf{S}(u,v) = m(m - 1) \sum\limits_{i=0}^n \sum\limits_{j=0}^m B_{i,n}(u) \left[ B_{j - 2,m - 2} - 2B_{j - 1,m - 2}(v) - B_{j,m - 2}(v) \right] \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` second derivatives w.r.t. :math:`v` along the :math:`u`-isoparametric curve of the Bézier surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bezier_surf_d2sdv2_iso_v(p: Iterable[Iterable[Iterable[float]]], nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`u` along an isoparametric curve in :math:`v` of a 
    Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u` linearly-spaced points 
    along the :math:`u`-direction according to

    .. math::

        \frac{\text{d}^2}{\text{d}v^2} \mathbf{S}(u,v) = m(m - 1) \sum\limits_{i=0}^n \sum\limits_{j=0}^m B_{i,n}(u) \left[ B_{j - 2,m - 2} - 2B_{j - 1,m - 2}(v) - B_{j,m - 2}(v) \right] \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` second derivatives w.r.t. :math:`u` along the :math:`v`-isoparametric curve of the Bézier surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bezier_surf_eval_grid(p: Iterable[Iterable[Iterable[float]]], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates a Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space according to

    .. math::

        \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m B_{i,n}(u) B_{j,m}(v) \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` points on the Bézier surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def bezier_surf_dsdu_grid(p: Iterable[Iterable[Iterable[float]]], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`u` on a Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space according to

    .. math::

        \frac{\text{d}}{\text{d}u} \mathbf{S}(u,v) = n \sum\limits_{i=0}^n \sum\limits_{j=0}^m \left[ B_{i - 1,n - 1}(u) - B_{i,n - 1}(u) \right] B_{j,m}(v) \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`u` on the Bézier surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def bezier_surf_dsdv_grid(p: Iterable[Iterable[Iterable[float]]], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`v` on a Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space according to

    .. math::

        \frac{\text{d}}{\text{d}v} \mathbf{S}(u,v) = m \sum\limits_{i=0}^n \sum\limits_{j=0}^m B_{i,n}(u) \left[ B_{j - 1,m - 1}(v) - B_{j,m - 1}(v) \right] \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`v` on the Bézier surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def bezier_surf_d2sdu2_grid(p: Iterable[Iterable[Iterable[float]]], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`u` on a Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space according to

    .. math::

        \frac{\text{d}^2}{\text{d}u^2} \mathbf{S}(u,v) = n(n-1) \sum\limits_{i=0}^n \sum\limits_{j=0}^m \left[ B_{i - 2,n - 2} - 2B_{i - 1,n - 2}(u) + B_{i,n - 2}(u) \right] B_{j,m}(v) \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`u` on the Bézier surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def bezier_surf_d2sdv2_grid(p: Iterable[Iterable[Iterable[float]]], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`v` on a Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space according to

    .. math::

        \frac{\text{d}^2}{\text{d}v^2} \mathbf{S}(u,v) = m(m - 1) \sum\limits_{i=0}^n \sum\limits_{j=0}^m B_{i,n}(u) \left[ B_{j - 2,m - 2} - 2B_{j - 1,m - 2}(v) - B_{j,m - 2}(v) \right] \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`v` on the Bézier surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def bezier_surf_eval_uvvecs(p: Iterable[Iterable[Iterable[float]]], u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates a Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs according to

    .. math::

        \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m B_{i,n}(u) B_{j,m}(v) \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of points on the Bézier surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bezier_surf_dsdu_uvvecs(p: Iterable[Iterable[Iterable[float]]], u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`u` on a Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs according to

    .. math::

        \frac{\text{d}}{\text{d}u} \mathbf{S}(u,v) = n \sum\limits_{i=0}^n \sum\limits_{j=0}^m \left[ B_{i - 1,n - 1}(u) - B_{i,n - 1}(u) \right] B_{j,m}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`u` on the Bézier surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bezier_surf_dsdv_uvvecs(p: Iterable[Iterable[Iterable[float]]], u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`v` on a Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs according to

    .. math::

        \frac{\text{d}}{\text{d}v} \mathbf{S}(u,v) = m \sum\limits_{i=0}^n \sum\limits_{j=0}^m B_{i,n}(u) \left[ B_{j - 1,m - 1}(v) - B_{j,m - 1}(v) \right] \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`v` on the Bézier surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bezier_surf_d2sdu2_uvvecs(p: Iterable[Iterable[Iterable[float]]], u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`u` on a Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs according to

    .. math::

        \frac{\text{d}^2}{\text{d}u^2} \mathbf{S}(u,v) = n(n-1) \sum\limits_{i=0}^n \sum\limits_{j=0}^m \left[ B_{i - 2,n - 2} - 2B_{i - 1,n - 2}(u) + B_{i,n - 2}(u) \right] B_{j,m}(v) \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`u` on the Bézier surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bezier_surf_d2sdv2_uvvecs(p: Iterable[Iterable[Iterable[float]]], u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`v` on a Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs according to

    .. math::

        \frac{\text{d}^2}{\text{d}v^2} \mathbf{S}(u,v) = m(m - 1) \sum\limits_{i=0}^n \sum\limits_{j=0}^m B_{i,n}(u) \left[ B_{j - 2,m - 2} - 2B_{j - 1,m - 2}(v) - B_{j,m - 2}(v) \right] \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`v` on the Bézier surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_curve_eval(p: Iterable[Iterable[float]], w: Iterable[float], t: float) -> List[float]:
    r"""
    Evaluates a rational Bézier curve with :math:`n+1` control points at a single :math:`t`-value according to

    .. math::

        \mathbf{C}(t) = \frac{\sum_{i=0}^n B_{i,n}(t) w_i \mathbf{P}_i}{\sum_{i=0}^n B_{i,n}(t) w_i}

    where :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    t: float
        Parameter value :math:`t` at which to evaluate
    
    Returns
    -------
    List[float]
        Value of the rational Bézier curve at :math:`t`. Has the same size as the inner dimension of ``p``
    """

def rational_bezier_curve_eval_dp(w: Iterable[float], i: int, n: int, dim: int, t: float) -> List[float]:
    r"""
    Evaluates the derivative of the rational Bézier curve with respect to an individual control point at a given :math:`t`-value
    
    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: float
        Parameter value at which to evaluate the curve sensitivity

    Returns
    -------
    List[float]
        1-D list representing the curve sensitivity at :math:`t` to the control point :math:`\mathbf{P}_i`
    """

def rational_bezier_curve_dcdt(p: Iterable[Iterable[float]], w: Iterable[float], t: float) -> List[float]:
    r"""
    Evaluates the first derivative (with respect to :math:`t`) of a rational Bézier curve with :math:`n+1` control 
    points at a single :math:`t`-value according to

    .. math::

        \frac{\text{d}}{\text{d}t} \mathbf{C}(t) = \frac{f'(t)g(t) - f(t)g'(t)}{g^2(t)}

    where

    .. math::

        \begin{align}
            f(t) &= \sum\limits_{i=0}^n B_{i,n}(t) w_i \mathbf{P}_i \\
            g(t) &= \sum\limits_{i=0}^n B_{i,n}(t) w_i \\
            f'(t) &= n \sum\limits_{i=0}^n \left[ B_{i-1,n-1}(t) - B_{i,n-1}(t) \right] w_i \mathbf{P}_i \\
            g'(t) &= n \sum\limits_{i=0}^n \left[ B_{i-1,n-1}(t) - B_{i,n-1}(t) \right] w_i
        \end{align}

    and :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    t: float
        Parameter value :math:`t` at which to evaluate
    
    Returns
    -------
    List[float]
        Value of the rational Bézier curve first derivative at :math:`t`. Has the same size as the inner dimension of ``p``
    """

def rational_bezier_curve_dcdt_dp(w: Iterable[float], i: int, n: int, dim: int, t: float) -> List[float]:
    r"""
    Evaluates the sensitivity of the rational Bézier curve first derivative with respect to an individual control point at a given :math:`t`-value
    
    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: float
        Parameter value at which to evaluate the curve first derivative sensitivity

    Returns
    -------
    List[float]
        1-D list representing the curve first derivative sensitivity at :math:`t` to the control point :math:`\mathbf{P}_i`
    """

def rational_bezier_curve_d2cdt2(p: Iterable[Iterable[float]], w: Iterable[float], t: float) -> List[float]:
    r"""
    Evaluates the second derivative (with respect to :math:`t`) of a rational Bézier curve with :math:`n+1` control 
    points at a single :math:`t`-value according to

    .. math::

        \frac{\text{d}^2}{\text{d}t^2} \mathbf{C}(t) = \frac{f''(t)g^2(t) - f(t)g(t)g''(t) - 2f'(t)g(t)g'(t) + 2f(t)[g'(t)]^2}{g^3(t)}

    where

    .. math::

        \begin{align}
            f(t) &= \sum\limits_{i=0}^n B_{i,n}(t) w_i \mathbf{P}_i \\
            g(t) &= \sum\limits_{i=0}^n B_{i,n}(t) w_i \\
            f'(t) &= n \sum\limits_{i=0}^n \left[ B_{i-1,n-1}(t) - B_{i,n-1}(t) \right] w_i \mathbf{P}_i \\
            g'(t) &= n \sum\limits_{i=0}^n \left[ B_{i-1,n-1}(t) - B_{i,n-1}(t) \right] w_i \\
            f''(t) &= n (n-1) \sum\limits_{i=0}^n \left[ B_{i-2,n-2}(t) - 2B_{i-1,n-2}(t) + B_{i,n-2}(t) \right] w_i \mathbf{P}_i \\
            g''(t) &= n (n-1) \sum\limits_{i=0}^n \left[ B_{i-2,n-2}(t) - 2B_{i-1,n-2}(t) + B_{i,n-2}(t) \right] w_i
        \end{align}

    and :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    t: float
        Parameter value :math:`t` at which to evaluate
    
    Returns
    -------
    List[float]
        Value of the rational Bézier curve first derivative at :math:`t`. Has the same size as the inner dimension of ``p``
    """

def rational_bezier_curve_d2cdt2_dp(w: Iterable[float], i: int, n: int, dim: int, t: float) -> List[float]:
    r"""
    Evaluates the sensitivity of the rational Bézier curve second derivative with respect to an individual control point at a given :math:`t`-value
    
    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: float
        Parameter value at which to evaluate the curve second derivative sensitivity

    Returns
    -------
    List[float]
        1-D list representing the curve second derivative sensitivity at :math:`t` to the control point :math:`\mathbf{P}_i`
    """

def rational_bezier_curve_eval_grid(p: Iterable[Iterable[float]], w: Iterable[float], nt: int) -> List[List[float]]:
    r"""
    Evaluates a rational Bézier curve with :math:`n+1` control points at :math:`N_t` linearly-spaced points according to

    .. math::

        \mathbf{C}(t) = \frac{\sum_{i=0}^n B_{i,n}(t) w_i \mathbf{P}_i}{\sum_{i=0}^n B_{i,n}(t) w_i}

    where :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.
    
    Returns
    -------
    List[List[float]]
        Value of the rational Bézier curve at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def rational_bezier_curve_eval_dp_grid(w: Iterable[float], i: int, n: int, dim: int, nt: int) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a rational Bézier curve with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the control point sensitivity of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the rational Bézier curve control point sensitivity at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def rational_bezier_curve_dcdt_grid(p: Iterable[Iterable[float]], w: Iterable[float], nt: int) -> List[List[float]]:
    r"""
    Evaluates the first derivative (with respect to :math:`t`) of a rational Bézier curve with :math:`n+1` control 
    points at :math:`N_t` linearly-spaced points according to

    .. math::

        \frac{\text{d}}{\text{d}t} \mathbf{C}(t) = \frac{f'(t)g(t) - f(t)g'(t)}{g^2(t)}

    where

    .. math::

        \begin{align}
            f(t) &= \sum\limits_{i=0}^n B_{i,n}(t) w_i \mathbf{P}_i \\
            g(t) &= \sum\limits_{i=0}^n B_{i,n}(t) w_i \\
            f'(t) &= n \sum\limits_{i=0}^n \left[ B_{i-1,n-1}(t) - B_{i,n-1}(t) \right] w_i \mathbf{P}_i \\
            g'(t) &= n \sum\limits_{i=0}^n \left[ B_{i-1,n-1}(t) - B_{i,n-1}(t) \right] w_i
        \end{align}

    and :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.
    
    Returns
    -------
    List[List[float]]
        Value of the rational Bézier curve first derivative at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def rational_bezier_curve_dcdt_dp_grid(w: Iterable[float], i: int, n: int, dim: int, nt: int) -> List[List[float]]:
    r"""
    Evaluates the first derivative sensitivity with respect to an individual control point of a rational Bézier curve with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the first derivative control point sensitivity of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the rational Bézier curve first derivative control point sensitivity at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def rational_bezier_curve_d2cdt2_grid(p: Iterable[Iterable[float]], w: Iterable[float], nt: int) -> List[List[float]]:
    r"""
    Evaluates the second derivative (with respect to :math:`t`) of a rational Bézier curve with :math:`n+1` control 
    points at :math:`N_t` linearly-spaced points according to

    where

    .. math::

        \begin{align}
            f(t) &= \sum\limits_{i=0}^n B_{i,n}(t) w_i \mathbf{P}_i \\
            g(t) &= \sum\limits_{i=0}^n B_{i,n}(t) w_i \\
            f'(t) &= n \sum\limits_{i=0}^n \left[ B_{i-1,n-1}(t) - B_{i,n-1}(t) \right] w_i \mathbf{P}_i \\
            g'(t) &= n \sum\limits_{i=0}^n \left[ B_{i-1,n-1}(t) - B_{i,n-1}(t) \right] w_i \\
            f''(t) &= n (n-1) \sum\limits_{i=0}^n \left[ B_{i-2,n-2}(t) - 2B_{i-1,n-2}(t) + B_{i,n-2}(t) \right] w_i \mathbf{P}_i \\
            g''(t) &= n (n-1) \sum\limits_{i=0}^n \left[ B_{i-2,n-2}(t) - 2B_{i-1,n-2}(t) + B_{i,n-2}(t) \right] w_i
        \end{align}

    and :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the rational Bézier curve first derivative at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def rational_bezier_curve_d2cdt2_dp_grid(w: Iterable[float], i: int, n: int, dim: int, nt: int) -> List[List[float]]:
    r"""
    Evaluates the second derivative sensitivity with respect to an individual control point of a rational Bézier curve with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the second derivative control point sensitivity of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the rational Bézier curve second derivative control point sensitivity at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def rational_bezier_curve_eval_tvec(p: Iterable[Iterable[float]], w: Iterable[float], t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates a rational Bézier curve with :math:`n+1` control points along a vector of :math:`t`-values according to

    .. math::

        \mathbf{C}(t) = \frac{\sum_{i=0}^n B_{i,n}(t) w_i \mathbf{P}_i}{\sum_{i=0}^n B_{i,n}(t) w_i}

    where :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    t: Iterable[float]
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.
    
    Returns
    -------
    List[List[float]]
        Value of the rational Bézier curve along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def rational_bezier_curve_eval_dp_tvec(w: Iterable[float], i: int, n: int, dim: int, t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a rational Bézier curve with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: Iterable[float]
        Parameter vector along which to evaluate the curve control point sensitivity

    Returns
    -------
    List[List[float]]
        Value of the rational Bézier curve control point sensitivity along parameter vector :math:`\mathbf{t}`. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def rational_bezier_curve_dcdt_tvec(p: Iterable[Iterable[float]], w: Iterable[float], t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates the first derivative (with respect to :math:`t`) of a rational Bézier curve with :math:`n+1` control 
    points along a vector of :math:`t`-values according to

    .. math::

        \frac{\text{d}}{\text{d}t} \mathbf{C}(t) = \frac{f'(t)g(t) - f(t)g'(t)}{g^2(t)}

    where

    .. math::

        \begin{align}
            f(t) &= \sum\limits_{i=0}^n B_{i,n}(t) w_i \mathbf{P}_i \\
            g(t) &= \sum\limits_{i=0}^n B_{i,n}(t) w_i \\
            f'(t) &= n \sum\limits_{i=0}^n \left[ B_{i-1,n-1}(t) - B_{i,n-1}(t) \right] w_i \mathbf{P}_i \\
            g'(t) &= n \sum\limits_{i=0}^n \left[ B_{i-1,n-1}(t) - B_{i,n-1}(t) \right] w_i
        \end{align}

    and :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    t: Iterable[float]
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.
    
    Returns
    -------
    List[List[float]]
        Value of the rational Bézier curve first derivative along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def rational_bezier_curve_dcdt_dp_tvec(w: Iterable[float], i: int, n: int, dim: int, t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a rational Bézier curve first derivative with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: Iterable[float]
        Parameter vector along which to evaluate the curve first derivative control point sensitivity

    Returns
    -------
    List[List[float]]
        Value of the rational Bézier curve first derivative control point sensitivity along parameter vector :math:`\mathbf{t}`. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def rational_bezier_curve_d2cdt2_tvec(p: Iterable[Iterable[float]], w: Iterable[float], t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates the second derivative (with respect to :math:`t`) of a rational Bézier curve with :math:`n+1` control 
    points along a vector of :math:`t`-values according to

    where

    .. math::

        \begin{align}
            f(t) &= \sum\limits_{i=0}^n B_{i,n}(t) w_i \mathbf{P}_i \\
            g(t) &= \sum\limits_{i=0}^n B_{i,n}(t) w_i \\
            f'(t) &= n \sum\limits_{i=0}^n \left[ B_{i-1,n-1}(t) - B_{i,n-1}(t) \right] w_i \mathbf{P}_i \\
            g'(t) &= n \sum\limits_{i=0}^n \left[ B_{i-1,n-1}(t) - B_{i,n-1}(t) \right] w_i \\
            f''(t) &= n (n-1) \sum\limits_{i=0}^n \left[ B_{i-2,n-2}(t) - 2B_{i-1,n-2}(t) + B_{i,n-2}(t) \right] w_i \mathbf{P}_i \\
            g''(t) &= n (n-1) \sum\limits_{i=0}^n \left[ B_{i-2,n-2}(t) - 2B_{i-1,n-2}(t) + B_{i,n-2}(t) \right] w_i
        \end{align}

    and :math:`B_{i,n}(t)` is the Bernstein polynomial.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but typical
        sizes include ``2`` (:math:`x`-:math:`y` space), ``3`` (:math:`x`-:math:`y`-:math:`z` space) and
        ``4`` (:math:`x`-:math:`y`-:math:`z`-:math:`w` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    t: Iterable[float]
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the rational Bézier curve first derivative along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def rational_bezier_curve_d2cdt2_dp_tvec(w: Iterable[float], i: int, n: int, dim: int, t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a rational Bézier curve second derivative with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    i: int
        Index of the control point
    n: int
        Degree of the curve (number of control points minus one)
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: Iterable[float]
        Parameter vector along which to evaluate the curve second derivative control point sensitivity

    Returns
    -------
    List[List[float]]
        Value of the rational Bézier curve second derivative control point sensitivity along parameter vector :math:`\mathbf{t}`. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def rational_bezier_surf_eval(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], u: float, v: float) -> List[float]:
    r"""
    Evaluates a rational Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair according to

    .. math::

        \mathbf{S}(u,v) = \frac{\sum_{i=0}^n \sum_{j=0}^m B_{i,n}(u) B_{j,m}(v) w_{i,j} \mathbf{P}_{i,j}}{\sum_{i=0}^n \sum_{j=0}^m B_{i,n}(u) B_{j,m}(v) w_{i,j}}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the rational Bézier surface at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def rational_bezier_surf_dsdu(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], u: float, v: float) -> List[float]:
    r"""
    Evaluates the first derivative w.r.t. :math:`u` of a rational Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the rational Bézier surface first derivative w.r.t. :math:`u` at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def rational_bezier_surf_dsdv(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], u: float, v: float) -> List[float]:
    r"""
    Evaluates the first derivative w.r.t. :math:`v` of a rational Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the rational Bézier surface first derivative w.r.t. :math:`v` at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def rational_bezier_surf_d2sdu2(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], u: float, v: float) -> List[float]:
    r"""
    Evaluates the second derivative w.r.t. :math:`u` of a rational Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the rational Bézier surface second derivative w.r.t. :math:`u` at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def rational_bezier_surf_d2sdv2(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], u: float, v: float) -> List[float]:
    r"""
    Evaluates the second derivative w.r.t. :math:`v` of a rational Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the rational Bézier surface second derivative w.r.t. :math:`v` at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def rational_bezier_surf_eval_dp(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, u: float, v: float) -> List[float]:
    r"""
    Evaluates the derivative of the rational Bézier surface with respect to an individual control point at a given :math:`(u,v)`-pair:

    .. math::

        \frac{\partial}{\partial \mathbf{P}_{i,j}} \mathbf{S}(u,v) = \frac{B_{i,n}(u) B_{j,m}(v) w_{i,j}}{\sum\limits_{ii=0}^n \sum\limits_{jj=0}^m B_{ii,n}(u) B_{jj,m}(v) w_{ii,jj}}
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[float]
        1-D list representing the surface sensitivity at :math:`(u,v)` to the control point :math:`\mathbf{P}_{i,j}`
    """

def rational_bezier_surf_dsdu_dp(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, u: float, v: float) -> List[float]:
    r"""
    Evaluates the derivative of the rational Bézier surface first :math:`u`-derivative with respect to an individual control point at a given :math:`(u,v)`-pair:

    .. math::

        \frac{\partial}{\partial \mathbf{P}_{i,j}} \left( \frac{\partial \mathbf{S}(u,v)}{\partial u} \right) = \frac{\frac{\partial f(u,v)}{\partial u} g(u,v) - f(u,v) \frac{\partial g(u,v)}{\partial u}}{g^2(u,v)}
    
    where

    .. math::

        \begin{align}
            f(u,v) &= B_{i,n}(u) B_{j,m}(v) w_{i,j} \\
            g(u,v) &= \sum\limits_{ii=0}^n \sum\limits_{jj=0}^m B_{ii,n}(u) B_{jj,m}(v) w_{ii,jj} \\
            \frac{\partial f(u,v)}{\partial u} &= n [B_{i-1,n-1}(u) - B_{i,n-1}(u)] B_{j,m}(v) w_{i,j} \\
            \frac{\partial g(u,v)}{\partial u} &= n \sum\limits_{ii=0}^n \sum\limits_{jj=0}^m [B_{ii-1,n-1}(u) - B_{ii,n-1}(u)] B_{jj,m}(v) w_{ii,jj}
        \end{align}

    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[float]
        1-D list representing the surface derivative sensitivity at :math:`(u,v)` to the control point :math:`\mathbf{P}_{i,j}`
    """

def rational_bezier_surf_dsdv_dp(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, u: float, v: float) -> List[float]:
    r"""
    Evaluates the derivative of the rational Bézier surface first :math:`v`-derivative with respect to an individual control point at a given :math:`(u,v)`-pair:

    .. math::

        \frac{\partial}{\partial \mathbf{P}_{i,j}} \left( \frac{\partial \mathbf{S}(u,v)}{\partial v} \right) = \frac{\frac{\partial f(u,v)}{\partial v} g(u,v) - f(u,v) \frac{\partial g(u,v)}{\partial v}}{g^2(u,v)}
    
    where

    .. math::

        \begin{align}
            f(u,v) &= B_{i,n}(u) B_{j,m}(v) w_{i,j} \\
            g(u,v) &= \sum\limits_{ii=0}^n \sum\limits_{jj=0}^m B_{ii,n}(u) B_{jj,m}(v) w_{ii,jj} \\
            \frac{\partial f(u,v)}{\partial v} &= m B_{i,n}(u) [B_{j-1,m-1}(v) - B_{j,m-1}(v)] w_{i,j} \\
            \frac{\partial g(u,v)}{\partial v} &= m \sum\limits_{ii=0}^n \sum\limits_{jj=0}^m B_{ii,n}(u) [B_{jj-1,m-1}(v) - B_{jj,m-1}(v)] w_{ii,jj}
        \end{align}

    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[float]
        1-D list representing the surface derivative sensitivity at :math:`(u,v)` to the control point :math:`\mathbf{P}_{i,j}`
    """

def rational_bezier_surf_d2sdu2_dp(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, u: float, v: float) -> List[float]:
    r"""
    Evaluates the derivative of the rational Bézier surface second :math:`u`-derivative with respect to an individual control point at a given :math:`(u,v)`-pair:

    .. math::

        \frac{\partial}{\partial \mathbf{P}_{i,j}} \left( \frac{\partial^2 \mathbf{S}(u,v)}{\partial u^2} \right) = \frac{\frac{\partial^2 f(u,v)}{\partial u^2} g^2(u, v) - f(u, v)g(u, v)\frac{\partial^2 g(u,v)}{\partial u^2} - 2\frac{\partial f(u,v)}{\partial u} g(u,v) \frac{\partial g(u,v)}{\partial u} + 2f(u, v)\left[ \frac{\partial g(u,v)}{\partial u} \right]^2}{g^3(u, v)}
    
    where

    .. math::

        \begin{align}
            f(u,v) &= B_{i,n}(u) B_{j,m}(v) w_{i,j} \\
            g(u,v) &= \sum\limits_{ii=0}^n \sum\limits_{jj=0}^m B_{ii,n}(u) B_{jj,m}(v) w_{ii,jj} \\
            \frac{\partial f(u,v)}{\partial u} &= n [B_{i-1,n-1}(u) - B_{i,n-1}(u)] B_{j,m}(v) w_{i,j} \\
            \frac{\partial g(u,v)}{\partial u} &= n \sum\limits_{ii=0}^n \sum\limits_{jj=0}^m [B_{ii-1,n-1}(u) - B_{ii,n-1}(u)] B_{jj,m}(v) w_{ii,jj} \\
            \frac{\partial^2 f(u,v)}{\partial u^2} &= n(n-1) [B_{i-2,n-2}(u) - 2 B_{i-1,n-2}(u) + B_{i,n-2}(u)] B_{j,m}(v) w_{i,j} \\
            \frac{\partial^2 g(u,v)}{\partial u^2} &= n(n-1) \sum\limits_{ii=0}^n \sum\limits_{jj=0}^m [B_{ii-2,n-2}(u)-2B_{ii-1,n-2}(u) + B_{ii,n-2}(u)] B_{jj,m}(v) w_{ii,jj}
        \end{align}
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[float]
        1-D list representing the surface derivative sensitivity at :math:`(u,v)` to the control point :math:`\mathbf{P}_{i,j}`
    """

def rational_bezier_surf_d2sdv2_dp(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, u: float, v: float) -> List[float]:
    r"""
    Evaluates the derivative of the rational Bézier surface second :math:`v`-derivative with respect to an individual control point at a given :math:`(u,v)`-pair:

    .. math::

        \frac{\partial}{\partial \mathbf{P}_{i,j}} \left( \frac{\partial^2 \mathbf{S}(u,v)}{\partial v^2} \right) = \frac{\frac{\partial^2 f(u,v)}{\partial v^2} g^2(u, v) - f(u, v)g(u, v)\frac{\partial^2 g(u,v)}{\partial v^2} - 2\frac{\partial f(u,v)}{\partial v} g(u,v) \frac{\partial g(u,v)}{\partial v} + 2f(u, v)\left[ \frac{\partial g(u,v)}{\partial v} \right]^2}{g^3(u, v)}
    
    where

    .. math::

        \begin{align}
            f(u,v) &= B_{i,n}(u) B_{j,m}(v) w_{i,j} \\
            g(u,v) &= \sum\limits_{ii=0}^n \sum\limits_{jj=0}^m B_{ii,n}(u) B_{jj,m}(v) w_{ii,jj} \\
            \frac{\partial f(u,v)}{\partial v} &= m B_{i,n}(u) [B_{j-1,m-1}(v) - B_{j,m-1}(v)] w_{i,j} \\
            \frac{\partial g(u,v)}{\partial v} &= m \sum\limits_{ii=0}^n \sum\limits_{jj=0}^m B_{ii,n}(u) [B_{jj-1,m-1}(v) - B_{jj,m-1}(v)] w_{ii,jj} \\
            \frac{\partial^2 f(u,v)}{\partial v^2} &= m(m-1) B_{i,n}(u) [B_{j-2,m-2}(v) - 2 B_{j-1,m-2}(v) + B_{j,m-2}(v)] w_{i,j} \\
            \frac{\partial^2 g(u,v)}{\partial v^2} &= m(m-1) \sum\limits_{ii=0}^n \sum\limits_{jj=0}^m  B_{ii,n}(u) [B_{jj-2,m-2}(v)-2B_{jj-1,m-2}(v) + B_{jj,m-2}(v)] w_{ii,jj}
        \end{align}

    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[float]
        1-D list representing the surface derivative sensitivity at :math:`(u,v)` to the control point :math:`\mathbf{P}_{i,j}`
    """

def rational_bezier_surf_eval_dp_iso_u(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the derivative of the rational Bézier surface with respect to an individual control point along a :math:`u`-isoparametric curve
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface sensitiviies
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def rational_bezier_surf_eval_dp_iso_v(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the derivative of the rational Bézier surface with respect to an individual control point along a :math:`v`-isoparametric curve
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface sensitivities
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_u \times d`, where :math:`d` is the number of spatial dimensions
    """

def rational_bezier_surf_dsdu_dp_iso_u(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the derivative of the rational Bézier surface first :math:`u`-derivative with respect to an individual control point along a :math:`u`-isoparametric curve
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface sensitiviies
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def rational_bezier_surf_dsdu_dp_iso_v(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the derivative of the rational Bézier surface first :math:`u`-derivative with respect to an individual control point along a :math:`v`-isoparametric curve
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface sensitivities
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_u \times d`, where :math:`d` is the number of spatial dimensions
    """

def rational_bezier_surf_dsdv_dp_iso_u(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the derivative of the rational Bézier surface first :math:`v`-derivative with respect to an individual control point along a :math:`u`-isoparametric curve
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface sensitiviies
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def rational_bezier_surf_dsdv_dp_iso_v(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the derivative of the rational Bézier surface first :math:`v`-derivative with respect to an individual control point along a :math:`v`-isoparametric curve
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface sensitivities
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_u \times d`, where :math:`d` is the number of spatial dimensions
    """

def rational_bezier_surf_d2sdu2_dp_iso_u(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the derivative of the rational Bézier surface second :math:`u`-derivative with respect to an individual control point along a :math:`u`-isoparametric curve
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface sensitiviies
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def rational_bezier_surf_d2sdu2_dp_iso_v(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the derivative of the rational Bézier surface second :math:`u`-derivative with respect to an individual control point along a :math:`v`-isoparametric curve
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface sensitivities
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_u \times d`, where :math:`d` is the number of spatial dimensions
    """

def rational_bezier_surf_d2sdv2_dp_iso_u(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the derivative of the rational Bézier surface second :math:`v`-derivative with respect to an individual control point along a :math:`u`-isoparametric curve
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface sensitivity
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface sensitiviies
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def rational_bezier_surf_d2sdv2_dp_iso_v(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the derivative of the rational Bézier surface second :math:`v`-derivative with respect to an individual control point along a :math:`v`-isoparametric curve
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface sensitivities
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface sensitivity
    
    Returns
    -------
    List[List[float]]
        2-D array of size :math:`N_u \times d`, where :math:`d` is the number of spatial dimensions
    """

def rational_bezier_surf_eval_dp_grid(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the derivative of the rational Bézier surface with respect to an individual control point on a :math:`(u,v)` grid
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface sensitiviies
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface sensitiviies

    Returns
    -------
    List[List[List[float]]]
        3-D array of size :math:`N_u \times N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def rational_bezier_surf_dsdu_dp_grid(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the derivative of the rational Bézier surface first :math:`u`-derivative with respect to an individual control point on a :math:`(u,v)` grid
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface derivative sensitiviies
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface derivative sensitiviies

    Returns
    -------
    List[List[List[float]]]
        3-D array of size :math:`N_u \times N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def rational_bezier_surf_dsdv_dp_grid(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the derivative of the rational Bézier surface first :math:`v`-derivative with respect to an individual control point on a :math:`(u,v)` grid
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface derivative sensitiviies
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface derivative sensitiviies

    Returns
    -------
    List[List[List[float]]]
        3-D array of size :math:`N_u \times N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def rational_bezier_surf_d2sdu2_dp_grid(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the derivative of the rational Bézier surface second :math:`u`-derivative with respect to an individual control point on a :math:`(u,v)` grid
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface derivative sensitiviies
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface derivative sensitiviies

    Returns
    -------
    List[List[List[float]]]
        3-D array of size :math:`N_u \times N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def rational_bezier_surf_d2sdv2_dp_grid(w: Iterable[Iterable[float]], i: int, j: int, n: int, m: int, dim: int, nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the derivative of the rational Bézier surface second :math:`v`-derivative with respect to an individual control point on a :math:`(u,v)` grid
    
    Parameters
    ----------
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    i: int
        Index :math:`i` (:math:`u`-direction) of the control point
    j: int
        Index :math:`j` (:math:`v`-direction) of the control point
    n: int
        Degree of the surface in the :math:`u`-direction
    m: int
        Degree of the surface in the :math:`v`-direction
    dim: int
        Number of spatial dimensions in the surface. Usually ``3``
    nu: int
        Number of linearly-spaced :math:`u`-values at which to evaluate the surface derivative sensitiviies
    nv: int
        Number of linearly-spaced :math:`v`-values at which to evaluate the surface derivative sensitiviies

    Returns
    -------
    List[List[List[float]]]
        3-D array of size :math:`N_u \times N_v \times d`, where :math:`d` is the number of spatial dimensions
    """

def rational_bezier_surf_eval_iso_u(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]],
                                    u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates an isoparametric curve in :math:`u` of a rational Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` points along the :math:`u`-isoparametric curve of the rational Bézier surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_surf_eval_iso_v(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]],
                                    nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates an isoparametric curve in :math:`v` of a rational Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` points along the :math:`v`-isoparametric curve of the rational Bézier surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_surf_dsdu_iso_u(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]],
                                    u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the first derivative w.r.t. :math:`u` along an isoparametric curve in :math:`u` of a rational Bézier 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` first derivatives w.r.t. :math:`u` along the :math:`u`-isoparametric curve of the rational Bézier surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_surf_dsdu_iso_v(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]],
                                    nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the first derivative w.r.t. :math:`u` along an isoparametric curve in :math:`v` of a rational Bézier 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` first derivatives w.r.t. :math:`u` along the :math:`v`-isoparametric curve of the rational Bézier surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_surf_dsdv_iso_u(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]],
                                    u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the first derivative w.r.t. :math:`v` along an isoparametric curve in :math:`u` of a rational Bézier 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` first derivatives w.r.t. :math:`v` along the :math:`u`-isoparametric curve of the rational Bézier surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_surf_dsdv_iso_v(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]],
                                    nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the first derivative w.r.t. :math:`v` along an isoparametric curve in :math:`v` of a rational Bézier 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` first derivatives w.r.t. :math:`v` along the :math:`v`-isoparametric curve of the rational Bézier surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_surf_d2sdu2_iso_u(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]],
                                      u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`u` along an isoparametric curve in :math:`u` of a rational Bézier 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` second derivatives w.r.t. :math:`u` along the :math:`u`-isoparametric curve of the rational Bézier surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_surf_d2sdu2_iso_v(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]],
                                      nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`u` along an isoparametric curve in :math:`v` of a rational Bézier 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` second derivatives w.r.t. :math:`u` along the :math:`v`-isoparametric curve of the rational Bézier surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_surf_d2sdv2_iso_u(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]],
                                      u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`v` along an isoparametric curve in :math:`u` of a rational Bézier 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` second derivatives w.r.t. :math:`v` along the :math:`u`-isoparametric curve of the rational Bézier surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_surf_d2sdv2_iso_v(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]],
                                      nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`v` along an isoparametric curve in :math:`v` of a rational Bézier 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` second derivatives w.r.t. :math:`v` along the :math:`v`-isoparametric curve of the rational Bézier surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_surf_eval_grid(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates a rational Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points along a 
    linearly-spaced rectangular grid in :math:`(u,v)`-space according to

    .. math::

        \mathbf{S}(u,v) = \frac{\sum_{i=0}^n \sum_{j=0}^m B_{i,n}(u) B_{j,m}(v) w_{i,j} \mathbf{P}_{i,j}}{\sum_{i=0}^n \sum_{j=0}^m B_{i,n}(u) B_{j,m}(v) w_{i,j}}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` points on the rational Bézier surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_surf_dsdu_grid(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                                   nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`u` on a rational Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`u` on the rational Bézier surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def rational_bezier_surf_dsdv_grid(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                                   nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`v` on a rational Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`v` on the rational Bézier surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def rational_bezier_surf_d2sdu2_grid(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                                     nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`u` on a rational Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`u` on the rational Bézier surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def rational_bezier_surf_d2sdv2_grid(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                                     nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`v` on a rational Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`v` on the rational Bézier surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def rational_bezier_surf_eval_uvvecs(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                                     u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates a rational Bézier surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of points on the rational Bézier surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_surf_dsdu_uvvecs(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                                     u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`u` on a rational Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`u` on the rational Bézier surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_surf_dsdv_uvvecs(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                                     u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`v` on a rational Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`v` on the rational Bézier surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_surf_d2sdu2_uvvecs(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                                       u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`u` on a rational Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`u` on the rational Bézier surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def rational_bezier_surf_d2sdv2_uvvecs(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                                       u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`v` on a rational Bézier surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`v` on the rational Bézier surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_curve_eval(p: Iterable[Iterable[float]], k: Iterable[float], t: float) -> List[float]:
    r"""
    Evaluates a B-spline curve with :math:`n+1` control points at a single :math:`t`-value according to

    .. math::

        \mathbf{C}(t) = \sum\limits_{i=0}^n N_{i,q}(t) \mathbf{P}_i

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`, defined recursively as

    .. math::

        N_{i,q} = \frac{t - t_i}{t_{i+q} - t_i} N_{i,q-1}(t) + \frac{t_{i+q+1} - t}{t_{i+q+1} - t_{i+1}} N_{i+1, q-1}(t)

    with base case

    .. math::

        N_{i,0} = \begin{cases}
            1, & \text{if } t_i \leq t < t_{i+1} \text{ and } t_i < t_{i+1} \\
            0, & \text{otherwise}
        \end{cases}

    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    k: Iterable[float]
        1-D list or array of knots
    t: float
        Parameter value :math:`t` at which to evaluate

    Returns
    -------
    List[float]
        Value of the B-spline curve at :math:`t`. Has the same size as the inner dimension of ``p``
    """

def bspline_curve_eval_dp(k: Iterable[float], i: int, q: int, dim: int, t: float) -> List[float]:
    r"""
    Evaluates the derivative of the B-spline curve with respect to an individual control point at a given :math:`t`-value
    
    Parameters
    ----------
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: float
        Parameter value at which to evaluate the curve sensitivity

    Returns
    -------
    List[float]
        1-D list representing the curve sensitivity at :math:`t` to the control point :math:`\mathbf{P}_i`
    """

def bspline_curve_dcdt(p: Iterable[Iterable[float]], k: Iterable[float], t: float) -> List[float]:
    r"""
    Evaluates the first derivative with respect to :math:`t` of a B-spline curve with :math:`n+1` 
    control points at a single :math:`t`-value according to

    .. math::

        \frac{\text{d}}{\text{d}t} \mathbf{C}(t) = \sum\limits_{i=0}^n N'_{i,q}(t) \mathbf{P}_i

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q` and its derivative is given by

    .. math::

        N'_{i,q}(t) = \frac{q}{k_{i+q} - k_i} N_{i,q-1}(t) - \frac{q}{k_{i+q+1} - k_{i+1}} N_{i+1,q-1}(t)

    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    k: Iterable[float]
        1-D list or array of knots
    t: float
        Parameter value :math:`t` at which to evaluate

    Returns
    -------
    List[float]
        Value of the first derivative w.r.t. :math:`t` of the B-spline curve at :math:`t`. Has the same size as the inner dimension of ``p``
    """

def bspline_curve_dcdt_dp(k: Iterable[float], i: int, q: int, dim: int, t: float) -> List[float]:
    r"""
    Evaluates the derivative of the B-spline curve first derivative with respect to an individual control point
  
    Parameters
    ----------
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: float
        Parameter value at which to evaluate the curve derivative sensitivity
    
    Returns
    -------
    List[float]
        1-D list representing the curve derivative sensitivity at :math:`t` to the control point :math:`\mathbf{P}_i`
    """

def bspline_curve_d2cdt2(p: Iterable[Iterable[float]], k: Iterable[float], t: float) -> List[float]:
    r"""
    Evaluates the second derivative with respect to :math:`t` of a B-spline curve with :math:`n+1` 
    control points at a single :math:`t`-value according to

    .. math::

        \frac{\text{d}^2}{\text{d}t^2} \mathbf{C}(t) = \sum\limits_{i=0}^n N''_{i,q}(t) \mathbf{P}_i

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q` and its second derivative is given by

    .. math::

        N''_{i,q}(t) = \frac{q}{k_{i+q} - k_i} \left[ \frac{q-1}{k_{i+q-1}-k_i} N_{i,q-2}(t) - \frac{q-1}{k_{i+q}-k_{i+1}} N_{i+1,q-2}(t) \right] - \frac{q}{k_{i+q+1} - k_{i+1}} \left[ \frac{q-1}{k_{i+q}-k_{i+1}} N_{i+1,q-2}(t) - \frac{q-1}{k_{i+q+1}-k_{i+2}} N_{i+2,q-2}(t) \right]

    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    k: Iterable[float]
        1-D list or array of knots
    t: float
        Parameter value :math:`t` at which to evaluate

    Returns
    -------
    List[float]
        Value of the second derivative w.r.t. :math:`t` of the B-spline curve at :math:`t`. Has the same size as the inner dimension of ``p``
    """

def bspline_curve_d2cdt2_dp(k: Iterable[float], i: int, q: int, dim: int, t: float) -> List[float]:
    r"""
    Evaluates the derivative of the Bézier curve second derivative with respect to an individual control point

    Parameters
    ----------
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: float
        Parameter value at which to evaluate the curve derivative sensitivity
    
    Returns
    -------
    List[float]
        1-D list representing the curve derivative sensitivity at :math:`t` to the control point :math:`\mathbf{P}_i`
    """

def bspline_curve_eval_grid(p: Iterable[Iterable[float]], k: Iterable[float], nt: int) -> List[List[float]]:
    r"""
    Evaluates a B-spline curve with :math:`n+1` control points on a 
    grid of linearly-spaced :math:`t`-values according to

    .. math::

        \mathbf{C}(t) = \sum\limits_{i=0}^n N_{i,q}(t) \mathbf{P}_i

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. 
    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    k: Iterable[float]
        1-D list or array of knots
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the B-spline curve at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def bspline_curve_eval_dp_grid(k: Iterable[float], i: int, q: int, dim: int, nt: int) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a B-spline curve with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the control point sensitivity of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the B-spline curve control point sensitivity at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def bspline_curve_dcdt_grid(p: Iterable[Iterable[float]], k: Iterable[float], nt: int) -> List[List[float]]:
    r"""
    Evaluates the first derivative with respect to :math:`t` of a B-spline curve 
    with :math:`n+1` control points on a grid of linearly-spaced :math:`t`-values according to

    .. math::

        \frac{\text{d}}{\text{d}t} \mathbf{C}(t) = \sum\limits_{i=0}^n N'_{i,q}(t) \mathbf{P}_i

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q` and its derivative is given by

    .. math::

        N'_{i,q}(t) = \frac{q}{k_{i+q} - k_i} N_{i,q-1}(t) - \frac{q}{k_{i+q+1} - k_{i+1}} N_{i+1,q-1}(t)

    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    k: Iterable[float]
        1-D list or array of knots
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the B-spline curve first derivatve w.r.t. :math:`t` at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def bspline_curve_dcdt_dp_grid(k: Iterable[float], i: int, q: int, dim: int, nt: int) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a B-spline curve first derivative with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the control point sensitivity of the curve first derivative at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the B-spline curve first derivative control point sensitivity at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def bspline_curve_d2cdt2_grid(p: Iterable[Iterable[float]], k: Iterable[float], nt: int) -> List[List[float]]:
    r"""
    Evaluates the second derivative with respect to :math:`t` of a B-spline curve 
    with :math:`n+1` control points on a grid of linearly-spaced :math:`t`-values according to

    .. math::

        \frac{\text{d}^2}{\text{d}t^2} \mathbf{C}(t) = \sum\limits_{i=0}^n N''_{i,q}(t) \mathbf{P}_i

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q` and its second derivative is given by

    .. math::

        N''_{i,q}(t) = \frac{q}{k_{i+q} - k_i} \left[ \frac{q-1}{k_{i+q-1}-k_i} N_{i,q-2}(t) - \frac{q-1}{k_{i+q}-k_{i+1}} N_{i+1,q-2}(t) \right] - \frac{q}{k_{i+q+1} - k_{i+1}} \left[ \frac{q-1}{k_{i+q}-k_{i+1}} N_{i+1,q-2}(t) - \frac{q-1}{k_{i+q+1}-k_{i+2}} N_{i+2,q-2}(t) \right]

    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    k: Iterable[float]
        1-D list or array of knots
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the B-spline curve second derivative w.r.t. :math:`t` at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def bspline_curve_d2cdt2_dp_grid(k: Iterable[float], i: int, q: int, dim: int, nt: int) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a B-spline curve second derivative with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the control point sensitivity of the curve second derivative at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the B-spline curve second derivative control point sensitivity at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def bspline_curve_eval_tvec(p: Iterable[Iterable[float]], k: Iterable[float], t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates a B-spline curve with :math:`n+1` control points on a 
    grid of linearly-spaced :math:`t`-values according to

    .. math::

        \mathbf{C}(t) = \sum\limits_{i=0}^n N_{i,q}(t) \mathbf{P}_i

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. 
    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    k: Iterable[float]
        1-D list or array of knots
    t: Iterable[float]
        Vector of parameter values

    Returns
    -------
    List[List[float]]
        Value of the B-spline curve along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def bspline_curve_eval_dp_tvec(k: Iterable[float], i: int, q: int, dim: int, t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a B-spline curve with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: Iterable[float]
        Vector of parameter values

    Returns
    -------
    List[List[float]]
        Value of the B-spline curve control point sensitivity along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def bspline_curve_dcdt_tvec(p: Iterable[Iterable[float]], k: Iterable[float], t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates the first derivative with respect to :math:`t` of a B-spline curve 
    with :math:`n+1` control points on a grid of linearly-spaced :math:`t`-values according to

    .. math::

        \frac{\text{d}}{\text{d}t} \mathbf{C}(t) = \sum\limits_{i=0}^n N'_{i,q}(t) \mathbf{P}_i

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q` and its derivative is given by

    .. math::

        N'_{i,q}(t) = \frac{q}{k_{i+q} - k_i} N_{i,q-1}(t) - \frac{q}{k_{i+q+1} - k_{i+1}} N_{i+1,q-1}(t)

    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    k: Iterable[float]
        1-D list or array of knots
    t: Iterable[float]
        Vector of parameter values

    Returns
    -------
    List[List[float]]
        Value of the B-spline curve first derivatve w.r.t. :math:`t` along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def bspline_curve_dcdt_dp_tvec(k: Iterable[float], i: int, q: int, dim: int, t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a B-spline curve first derivative with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: Iterable[float]
        Vector of parameter values

    Returns
    -------
    List[List[float]]
        Value of the B-spline curve first derivative control point sensitivity along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def bspline_curve_d2cdt2_tvec(p: Iterable[Iterable[float]], k: Iterable[float], t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates the second derivative with respect to :math:`t` of a B-spline curve 
    with :math:`n+1` control points on a grid of linearly-spaced :math:`t`-values according to

    .. math::

        \frac{\text{d}^2}{\text{d}t^2} \mathbf{C}(t) = \sum\limits_{i=0}^n N''_{i,q}(t) \mathbf{P}_i

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q` and its second derivative is given by

    .. math::

        N''_{i,q}(t) = \frac{q}{k_{i+q} - k_i} \left[ \frac{q-1}{k_{i+q-1}-k_i} N_{i,q-2}(t) - \frac{q-1}{k_{i+q}-k_{i+1}} N_{i+1,q-2}(t) \right] - \frac{q}{k_{i+q+1} - k_{i+1}} \left[ \frac{q-1}{k_{i+q}-k_{i+1}} N_{i+1,q-2}(t) - \frac{q-1}{k_{i+q+1}-k_{i+2}} N_{i+2,q-2}(t) \right]

    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    k: Iterable[float]
        1-D list or array of knots
    t: Iterable[float]
        Vector of parameter values

    Returns
    -------
    List[List[float]]
        Value of the B-spline curve second derivative w.r.t. :math:`t` along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def bspline_curve_d2cdt2_dp_tvec(k: Iterable[float], i: int, q: int, dim: int, t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates the sensitivity with respect to an individual control point of a B-spline curve second derivative with 
    :math:`n+1` control points at :math:`N_t` linearly-spaced points in :math:`t`

    Parameters
    ----------
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: Iterable[float]
        Vector of parameter values

    Returns
    -------
    List[List[float]]
        Value of the B-spline curve second derivative control point sensitivity along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``2`` or ``3``)
    """

def bspline_surf_eval(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], u: float, v: float) -> List[float]:
    r"""
    Evaluates a B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair according to

    .. math::

        \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N_{i,q}(u) N_{j,r}(v) \mathbf{P}_{i,j}

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. The degree of the B-spline
    in the :math:`u`-direction is computed as ``q = len(ku) - len(p) - 1``, and the degree of the B-spline
    surface in the :math:`v`-direction is computed as ``r = len(kv) - len(p[0]) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the B-spline surface at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def bspline_surf_dsdu(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], u: float, v: float) -> List[float]:
    r"""
    Evaluates a the first derivative w.r.t. :math:`u` of a B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair according to

    .. math::

        \frac{\partial}{\partial u} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N'_{i,q}(u) N_{j,r}(v) \mathbf{P}_{i,j}

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. The degree of the B-spline
    in the :math:`u`-direction is computed as ``q = len(ku) - len(p) - 1``, and the degree of the B-spline
    surface in the :math:`v`-direction is computed as ``r = len(kv) - len(p[0]) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the first derivative w.r.t. :math:`u` of the B-spline surface at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def bspline_surf_dsdv(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], u: float, v: float) -> List[float]:
    r"""
    Evaluates a the first derivative w.r.t. :math:`v` of a B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair according to

    .. math::

        \frac{\partial}{\partial v} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N_{i,q}(u) N'_{j,r}(v) \mathbf{P}_{i,j}

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. The degree of the B-spline
    in the :math:`u`-direction is computed as ``q = len(ku) - len(p) - 1``, and the degree of the B-spline
    surface in the :math:`v`-direction is computed as ``r = len(kv) - len(p[0]) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the first derivative w.r.t. :math:`v` of the B-spline surface at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def bspline_surf_d2sdu2(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], u: float, v: float) -> List[float]:
    r"""
    Evaluates a the second derivative w.r.t. :math:`u` of a B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair according to

    .. math::

        \frac{\partial^2}{\partial u^2} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N''_{i,q}(u) N_{j,r}(v) \mathbf{P}_{i,j}

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. The degree of the B-spline
    in the :math:`u`-direction is computed as ``q = len(ku) - len(p) - 1``, and the degree of the B-spline
    surface in the :math:`v`-direction is computed as ``r = len(kv) - len(p[0]) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the second derivative w.r.t. :math:`u` of the B-spline surface at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def bspline_surf_d2sdv2(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], u: float, v: float) -> List[float]:
    r"""
    Evaluates a the second derivative w.r.t. :math:`v` of a B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair according to

    .. math::

        \frac{\partial^2}{\partial v^2} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N_{i,q}(u) N''_{j,r}(v) \mathbf{P}_{i,j}

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. The degree of the B-spline
    in the :math:`u`-direction is computed as ``q = len(ku) - len(p) - 1``, and the degree of the B-spline
    surface in the :math:`v`-direction is computed as ``r = len(kv) - len(p[0]) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the second derivative w.r.t. :math:`v` of the B-spline surface at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def bspline_surf_eval_iso_u(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates an isoparametric curve in :math:`u` of a B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction according to

    .. math::

        \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N_{i,q}(u) N_{j,r}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` points along the :math:`u`-isoparametric curve of the B-spline surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_surf_eval_iso_v(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates an isoparametric curve in :math:`v` of a B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u` linearly-spaced points 
    along the :math:`u`-direction according to

    .. math::

        \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N_{i,q}(u) N_{j,r}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` points along the :math:`v`-isoparametric curve of the B-spline surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_surf_dsdu_iso_u(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the first derivative w.r.t. :math:`u` along an isoparametric curve in :math:`u` of a 
    B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction according to

    .. math::

        \frac{\partial}{\partial u} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N'_{i,q}(u) N_{j,r}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` first derivatives w.r.t. :math:`u` along the :math:`u`-isoparametric curve of the B-spline surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_surf_dsdu_iso_v(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the first derivative w.r.t. :math:`u` along an isoparametric curve in :math:`v` of a 
    B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u` linearly-spaced points 
    along the :math:`u`-direction according to

    .. math::

        \frac{\partial}{\partial u} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N'_{i,q}(u) N_{j,r}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` first derivatives w.r.t. :math:`u` along the :math:`v`-isoparametric curve of the B-spline surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_surf_dsdv_iso_u(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`v` along an isoparametric curve in :math:`u` of a 
    B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction according to

    .. math::

        \frac{\partial}{\partial v} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N_{i,q}(u) N'_{j,r}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` first derivatives w.r.t. :math:`v` along the :math:`u`-isoparametric curve of the B-spline surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_surf_dsdv_iso_v(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the first derivative w.r.t. :math:`u` along an isoparametric curve in :math:`v` of a 
    B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u` linearly-spaced points 
    along the :math:`u`-direction according to

    .. math::

        \frac{\partial}{\partial v} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N_{i,q}(u) N'_{j,r}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` first derivatives w.r.t. :math:`u` along the :math:`v`-isoparametric curve of the B-spline surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_surf_d2sdu2_iso_u(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`u` along an isoparametric curve in :math:`u` of a 
    B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction according to

    .. math::

        \frac{\partial^2}{\partial u^2} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N''_{i,q}(u) N_{j,r}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` second derivatives w.r.t. :math:`u` along the :math:`u`-isoparametric curve of the B-spline surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_surf_d2sdu2_iso_v(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`u` along an isoparametric curve in :math:`v` of a 
    B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u` linearly-spaced points 
    along the :math:`u`-direction according to

    .. math::

        \frac{\partial^2}{\partial u^2} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N''_{i,q}(u) N_{j,r}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` second derivatives w.r.t. :math:`u` along the :math:`v`-isoparametric curve of the B-spline surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_surf_d2sdv2_iso_u(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`v` along an isoparametric curve in :math:`u` of a 
    B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction according to

    .. math::

        \frac{\partial^2}{\partial v^2} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N_{i,q}(u) N''_{j,r}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` second derivatives w.r.t. :math:`v` along the :math:`u`-isoparametric curve of the B-spline surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_surf_d2sdv2_iso_v(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`u` along an isoparametric curve in :math:`v` of a 
    B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u` linearly-spaced points 
    along the :math:`u`-direction according to

    .. math::

        \frac{\partial^2}{\partial v^2} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N_{i,q}(u) N''_{j,r}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` second derivatives w.r.t. :math:`u` along the :math:`v`-isoparametric curve of the B-spline surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_surf_eval_grid(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates a B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` 
    points along a linearly-spaced rectangular grid in :math:`(u,v)`-space according to

    .. math::

        \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N_{i,q}(u) N_{j,r}(v) \mathbf{P}_{i,j}
    
    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. The degree of the B-spline
    in the :math:`u`-direction is computed as ``q = len(ku) - len(p) - 1``, and the degree of the B-spline
    surface in the :math:`v`-direction is computed as ``r = len(kv) - len(p[0]) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` points on the B-spline surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_surf_dsdu_grid(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`u` on a B-spline surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space according to

    .. math::

        \frac{\partial}{\partial u} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N'_{i,q}(u) N_{j,r}(v) \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`u` on the B-spline surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def bspline_surf_dsdv_grid(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`v` on a B-spline surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space according to

    .. math::

        \frac{\partial}{\partial v} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N_{i,q}(u) N'_{j,r}(v) \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`v` on the B-spline surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def bspline_surf_d2sdu2_grid(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`u` on a B-spline surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space according to

    .. math::

        \frac{\partial^2}{\partial u^2} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N''_{i,q}(u) N_{j,r}(v) \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`u` on the B-spline surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def bspline_surf_d2sdv2_grid(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`v` on a B-spline surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space according to

    .. math::

        \frac{\partial^2}{\partial v^2} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N_{i,q}(u) N''_{j,r}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`v` on the B-spline surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def bspline_surf_eval_uvvecs(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates a B-spline surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs according to

    .. math::

        \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N_{i,q}(u) N_{j,r}(v) \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of points on the B-spline surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_surf_dsdu_uvvecs(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`u` on a B-spline surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs according to

    .. math::

        \frac{\partial}{\partial u} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N'_{i,q}(u) N_{j,r}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`u` on the B-spline surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_surf_dsdv_uvvecs(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`v` on a B-spline surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs according to

    .. math::

        \frac{\partial}{\partial v} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N_{i,q}(u) N'_{j,r}(v) \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`v` on the B-spline surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_surf_d2sdu2_uvvecs(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`u` on a B-spline surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs according to

    .. math::

        \frac{\partial^2}{\partial u^2} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N''_{i,q}(u) N_{j,r}(v) \mathbf{P}_{i,j}
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`u` on the B-spline surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def bspline_surf_d2sdv2_uvvecs(p: Iterable[Iterable[Iterable[float]]], ku: Iterable[float], kv: Iterable[float], u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`v` on a B-spline surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs according to

    .. math::

        \frac{\partial^2}{\partial v^2} \mathbf{S}(u,v) = \sum\limits_{i=0}^n \sum\limits_{j=0}^m N_{i,q}(u) N''_{j,r}(v) \mathbf{P}_{i,j}

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`v` on the B-spline surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_curve_eval(p: Iterable[Iterable[float]], w: Iterable[float], k: Iterable[float], t: float) -> List[float]:
    r"""
    Evaluates a Non-Uniform Rational B-Spline (NURBS) curve with :math:`n+1` control points at a 
    single :math:`t`-value according to

    .. math::

        \mathbf{C}(t) = \frac{\sum_{i=0}^n N_{i,q}(t) w_i \mathbf{P}_i}{\sum_{i=0}^n N_{i,q}(t) w_i}

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. 
    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    t: float
        Parameter value :math:`t` at which to evaluate

    Returns
    -------
    List[float]
        Value of the NURBS curve at :math:`t`. Has the same size as the inner dimension of ``p``
    """

def nurbs_curve_eval_dp(w: Iterable[float], k: Iterable[float], i: int, q: int, dim: int, t: float) -> List[float]:
    r"""
    Evaluates the derivative of the NURBS curve with respect to an individual control point at a given :math:`t`-value

    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: float
        Parameter value at which to evaluate the curve sensitivity

    Returns
    -------
    List[float]
        1-D list representing the curve sensitivity at :math:`t` to the control point :math:`\mathbf{P}_i`
    """

def nurbs_curve_dcdt(p: Iterable[Iterable[float]], w: Iterable[float], k: Iterable[float], t: float) -> List[float]:
    r"""
    Evaluates a the first derivative with respect to :math:`t` of a Non-Uniform Rational B-Spline (NURBS) curve 
    with :math:`n+1` control points at a single :math:`t`-value according to

    .. math::

        \frac{\text{d}}{\text{d}t} \mathbf{C}(t) = \frac{f'(t)g(t)-f(t)g'(t)}{g^2(t)}

    where

    .. math::

        \begin{align}
            f(t) &= \sum\limits_{i=0}^n N_{i,q}(t) w_i \mathbf{P}_i \\
            g(t) &= \sum\limits_{i=0}^n N_{i,q}(t) w_i \\
            f'(t) &= \sum\limits_{i=0}^n N'_{i,q}(t) w_i \mathbf{P}_i \\
            g'(t) &= \sum\limits_{i=0}^n N'_{i,q}(t) w_i \\
            N'_{i,q}(t) &= \frac{q}{k_{i+q} - k_i} N_{i,q-1}(t) - \frac{q}{k_{i+q+1} - k_{i+1}} N_{i+1,q-1}(t) \\
        \end{align}

    and :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. 
    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    t: float
        Parameter value :math:`t` at which to evaluate

    Returns
    -------
    List[float]
        Value of the NURBS curve derivative w.r.t. :math:`t` at :math:`t`. Has the same size as the inner dimension of ``p``
    """

def nurbs_curve_dcdt_dp(w: Iterable[float], k: Iterable[float], i: int, q: int, dim: int, t: float) -> List[float]:
    r"""
    Evaluates the sensitivity of the NURBS curve first derivative with respect to an individual control point at a given :math:`t`-value

    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: float
        Parameter value at which to evaluate the curve sensitivity

    Returns
    -------
    List[float]
        1-D list representing the curve first derivative sensitivity at :math:`t` to the control point :math:`\mathbf{P}_i`
    """

def nurbs_curve_d2cdt2(p: Iterable[Iterable[float]], w: Iterable[float], k: Iterable[float], t: float) -> List[float]:
    r"""
    Evaluates a the second derivative with respect to :math:`t` of a Non-Uniform Rational B-Spline (NURBS) curve 
    with :math:`n+1` control points at a single :math:`t`-value according to

    .. math::

        \frac{\text{d}^2}{\text{d}t^2} \mathbf{C}(t) = \frac{f''(t)g^2(t) - f(t)g(t)g''(t) - 2f'(t)g(t)g'(t) + 2f(t)[g'(t)]^2}{g^3(t)}

    where

    .. math::

        \begin{align}
            f(t) &= \sum\limits_{i=0}^n N_{i,q}(t) w_i \mathbf{P}_i \\
            g(t) &= \sum\limits_{i=0}^n N_{i,q}(t) w_i \\
            f'(t) &= \sum\limits_{i=0}^n N'_{i,q}(t) w_i \mathbf{P}_i \\
            g'(t) &= \sum\limits_{i=0}^n N'_{i,q}(t) w_i \\
            f''(t) &= \sum\limits_{i=0}^n N''_{i,q}(t) w_i \mathbf{P}_i \\
            g''(t) &= \sum\limits_{i=0}^n N''_{i,q}(t) w_i \\
            N'_{i,q}(t) &= \frac{q}{k_{i+q} - k_i} N_{i,q-1}(t) - \frac{q}{k_{i+q+1} - k_{i+1}} N_{i+1,q-1}(t) \\
            N''_{i,q}(t) &= \frac{q}{k_{i+q} - k_i} \left[ \frac{q-1}{k_{i+q-1}-k_i} N_{i,q-2}(t) - \frac{q-1}{k_{i+q}-k_{i+1}} N_{i+1,q-2}(t) \right] - \frac{q}{k_{i+q+1} - k_{i+1}} \left[ \frac{q-1}{k_{i+q}-k_{i+1}} N_{i+1,q-2}(t) - \frac{q-1}{k_{i+q+1}-k_{i+2}} N_{i+2,q-2}(t) \right]
        \end{align}

    and :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. 
    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    t: float
        Parameter value :math:`t` at which to evaluate

    Returns
    -------
    List[float]
        Value of the NURBS curve second derivative w.r.t. :math:`t` at :math:`t`. Has the same size as the inner dimension of ``p``
    """

def nurbs_curve_d2cdt2_dp(w: Iterable[float], k: Iterable[float], i: int, q: int, dim: int, t: float) -> List[float]:
    r"""
    Evaluates the sensitivity of the NURBS curve second derivative with respect to an individual control point at a given :math:`t`-value

    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: float
        Parameter value at which to evaluate the curve sensitivity

    Returns
    -------
    List[float]
        1-D list representing the curve second derivative sensitivity at :math:`t` to the control point :math:`\mathbf{P}_i`
    """

def nurbs_curve_eval_grid(p: Iterable[Iterable[float]], w: Iterable[float], k: Iterable[float], nt: int) -> List[List[float]]:
    r"""
    Evaluates a Non-Uniform Rational B-Spline (NURBS) curve with :math:`n+1` control points on a 
    grid of linearly-spaced :math:`t`-values according to

    .. math::

        \mathbf{C}(t) = \frac{\sum_{i=0}^n N_{i,q}(t) w_i \mathbf{P}_i}{\sum_{i=0}^n N_{i,q}(t) w_i}

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. 
    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the NURBS curve at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def nurbs_curve_eval_dp_grid(w: Iterable[float], k: Iterable[float], i: int, q: int, dim: int, nt: int) -> List[float]:
    r"""
    Evaluates the derivative of the NURBS curve with respect to an individual control point at a given :math:`t`-value

    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the NURBS curve sensitivity w.r.t. :math:`\mathbf{P}_i` at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def nurbs_curve_dcdt_grid(p: Iterable[Iterable[float]], w: Iterable[float], k: Iterable[float], nt: int) -> List[List[float]]:
    r"""
    Evaluates a the first derivative with respect to :math:`t` of a Non-Uniform Rational B-Spline (NURBS) curve 
    with :math:`n+1` control points on a grid of linearly-spaced :math:`t`-values according to

    .. math::

        \frac{\text{d}}{\text{d}t} \mathbf{C}(t) = \frac{f'(t)g(t)-f(t)g'(t)}{g^2(t)}

    where

    .. math::

        \begin{align}
            f(t) &= \sum\limits_{i=0}^n N_{i,q}(t) w_i \mathbf{P}_i \\
            g(t) &= \sum\limits_{i=0}^n N_{i,q}(t) w_i \\
            f'(t) &= \sum\limits_{i=0}^n N'_{i,q}(t) w_i \mathbf{P}_i \\
            g'(t) &= \sum\limits_{i=0}^n N'_{i,q}(t) w_i \\
            N'_{i,q}(t) &= \frac{q}{k_{i+q} - k_i} N_{i,q-1}(t) - \frac{q}{k_{i+q+1} - k_{i+1}} N_{i+1,q-1}(t) \\
        \end{align}

    and :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. 
    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the NURBS curve first derivatve w.r.t. :math:`t` at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def nurbs_curve_dcdt_dp_grid(w: Iterable[float], k: Iterable[float], i: int, q: int, dim: int, nt: int) -> List[float]:
    r"""
    Evaluates the sensitivity of the NURBS curve first derivative with respect to an individual control point at a given :math:`t`-value

    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the NURBS curve first derivative sensitivity w.r.t. :math:`\mathbf{P}_i` at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def nurbs_curve_d2cdt2_grid(p: Iterable[Iterable[float]], w: Iterable[float], k: Iterable[float], nt: int) -> List[List[float]]:
    r"""
    Evaluates a the second derivative with respect to :math:`t` of a Non-Uniform Rational B-Spline (NURBS) curve 
    with :math:`n+1` control points on a grid of linearly-spaced :math:`t`-values according to

    .. math::

        \frac{\text{d}^2}{\text{d}t^2} \mathbf{C}(t) = \frac{f''(t)g^2(t) - f(t)g(t)g''(t) - 2f'(t)g(t)g'(t) + 2f(t)[g'(t)]^2}{g^3(t)}

    where

    .. math::

        \begin{align}
            f(t) &= \sum\limits_{i=0}^n N_{i,q}(t) w_i \mathbf{P}_i \\
            g(t) &= \sum\limits_{i=0}^n N_{i,q}(t) w_i \\
            f'(t) &= \sum\limits_{i=0}^n N'_{i,q}(t) w_i \mathbf{P}_i \\
            g'(t) &= \sum\limits_{i=0}^n N'_{i,q}(t) w_i \\
            f''(t) &= \sum\limits_{i=0}^n N''_{i,q}(t) w_i \mathbf{P}_i \\
            g''(t) &= \sum\limits_{i=0}^n N''_{i,q}(t) w_i \\
            N'_{i,q}(t) &= \frac{q}{k_{i+q} - k_i} N_{i,q-1}(t) - \frac{q}{k_{i+q+1} - k_{i+1}} N_{i+1,q-1}(t) \\
            N''_{i,q}(t) &= \frac{q}{k_{i+q} - k_i} \left[ \frac{q-1}{k_{i+q-1}-k_i} N_{i,q-2}(t) - \frac{q-1}{k_{i+q}-k_{i+1}} N_{i+1,q-2}(t) \right] - \frac{q}{k_{i+q+1} - k_{i+1}} \left[ \frac{q-1}{k_{i+q}-k_{i+1}} N_{i+1,q-2}(t) - \frac{q-1}{k_{i+q+1}-k_{i+2}} N_{i+2,q-2}(t) \right]
        \end{align}

    and :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. 
    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the NURBS curve second derivative w.r.t. :math:`t` at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def nurbs_curve_d2cdt2_dp_grid(w: Iterable[float], k: Iterable[float], i: int, q: int, dim: int, nt: int) -> List[float]:
    r"""
    Evaluates the sensitivity of the NURBS curve second derivative with respect to an individual control point at a given :math:`t`-value

    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
        1-D list or array of knots
    nt: int
        Number of linearly-spaced points in :math:`t`. E.g., ``nt=3`` outputs
        the evaluation of the curve at :math:`t=0.0`, :math:`t=0.5`, and :math:`t=1.0`.

    Returns
    -------
    List[List[float]]
        Value of the NURBS curve second derivative sensitivity w.r.t. :math:`\mathbf{P}_i` at :math:`N_t` linearly-spaced points. Output array has size
        :math:`N_t \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def nurbs_curve_eval_tvec(p: Iterable[Iterable[float]], w: Iterable[float], k: Iterable[float], t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates a Non-Uniform Rational B-Spline (NURBS) curve with :math:`n+1` control points on a 
    grid of linearly-spaced :math:`t`-values according to

    .. math::

        \mathbf{C}(t) = \frac{\sum_{i=0}^n N_{i,q}(t) w_i \mathbf{P}_i}{\sum_{i=0}^n N_{i,q}(t) w_i}

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. 
    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    t: Iterable[float]
        Vector of parameter values

    Returns
    -------
    List[List[float]]
        Value of the NURBS curve along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def nurbs_curve_eval_dp_tvec(w: Iterable[float], k: Iterable[float], i: int, q: int, dim: int, t: Iterable[float]) -> List[float]:
    r"""
    Evaluates the derivative of the NURBS curve with respect to an individual control point at a given :math:`t`-value

    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: Iterable[float]
        Vector of parameter values

    Returns
    -------
    List[List[float]]
        Value of the NURBS curve sensitivity w.r.t. :math:`\mathbf{P}_i` along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def nurbs_curve_dcdt_tvec(p: Iterable[Iterable[float]], w: Iterable[float], k: Iterable[float], t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates a the first derivative with respect to :math:`t` of a Non-Uniform Rational B-Spline (NURBS) curve 
    with :math:`n+1` control points on a grid of linearly-spaced :math:`t`-values according to

    .. math::

        \frac{\text{d}}{\text{d}t} \mathbf{C}(t) = \frac{f'(t)g(t)-f(t)g'(t)}{g^2(t)}

    where

    .. math::

        \begin{align}
            f(t) &= \sum\limits_{i=0}^n N_{i,q}(t) w_i \mathbf{P}_i \\
            g(t) &= \sum\limits_{i=0}^n N_{i,q}(t) w_i \\
            f'(t) &= \sum\limits_{i=0}^n N'_{i,q}(t) w_i \mathbf{P}_i \\
            g'(t) &= \sum\limits_{i=0}^n N'_{i,q}(t) w_i \\
            N'_{i,q}(t) &= \frac{q}{k_{i+q} - k_i} N_{i,q-1}(t) - \frac{q}{k_{i+q+1} - k_{i+1}} N_{i+1,q-1}(t) \\
        \end{align}

    and :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. 
    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    t: Iterable[float]
        Vector of parameter values

    Returns
    -------
    List[List[float]]
        Value of the NURBS curve first derivatve w.r.t. :math:`t` along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def nurbs_curve_dcdt_dp_tvec(w: Iterable[float], k: Iterable[float], i: int, q: int, dim: int, t: Iterable[float]) -> List[float]:
    r"""
    Evaluates the sensitivity of the NURBS curve first derivative with respect to an individual control point at a given :math:`t`-value

    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
    t: Iterable[float]
        Vector of parameter values

    Returns
    -------
    List[List[float]]
        Value of the NURBS curve first derivative sensitivity w.r.t. :math:`\mathbf{P}_i` along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def nurbs_curve_d2cdt2_tvec(p: Iterable[Iterable[float]], w: Iterable[float], k: Iterable[float], t: Iterable[float]) -> List[List[float]]:
    r"""
    Evaluates a the second derivative with respect to :math:`t` of a Non-Uniform Rational B-Spline (NURBS) curve 
    with :math:`n+1` control points on a grid of linearly-spaced :math:`t`-values according to

    .. math::

        \frac{\text{d}^2}{\text{d}t^2} \mathbf{C}(t) = \frac{f''(t)g^2(t) - f(t)g(t)g''(t) - 2f'(t)g(t)g'(t) + 2f(t)[g'(t)]^2}{g^3(t)}

    where

    .. math::

        \begin{align}
            f(t) &= \sum\limits_{i=0}^n N_{i,q}(t) w_i \mathbf{P}_i \\
            g(t) &= \sum\limits_{i=0}^n N_{i,q}(t) w_i \\
            f'(t) &= \sum\limits_{i=0}^n N'_{i,q}(t) w_i \mathbf{P}_i \\
            g'(t) &= \sum\limits_{i=0}^n N'_{i,q}(t) w_i \\
            f''(t) &= \sum\limits_{i=0}^n N''_{i,q}(t) w_i \mathbf{P}_i \\
            g''(t) &= \sum\limits_{i=0}^n N''_{i,q}(t) w_i \\
            N'_{i,q}(t) &= \frac{q}{k_{i+q} - k_i} N_{i,q-1}(t) - \frac{q}{k_{i+q+1} - k_{i+1}} N_{i+1,q-1}(t) \\
            N''_{i,q}(t) &= \frac{q}{k_{i+q} - k_i} \left[ \frac{q-1}{k_{i+q-1}-k_i} N_{i,q-2}(t) - \frac{q-1}{k_{i+q}-k_{i+1}} N_{i+1,q-2}(t) \right] - \frac{q}{k_{i+q+1} - k_{i+1}} \left[ \frac{q-1}{k_{i+q}-k_{i+1}} N_{i+1,q-2}(t) - \frac{q-1}{k_{i+q+1}-k_{i+2}} N_{i+2,q-2}(t) \right]
        \end{align}

    and :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. 
    The degree of the B-spline is computed as ``q = len(k) - len(p) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[float]]
        2-D list or array of control points where the inner dimension can have any size, but the typical 
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    t: Iterable[float]
        Vector of parameter values

    Returns
    -------
    List[List[float]]
        Value of the NURBS curve second derivative w.r.t. :math:`t` along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def nurbs_curve_d2cdt2_dp_tvec(w: Iterable[float], k: Iterable[float], i: int, q: int, dim: int, t: Iterable[float]) -> List[float]:
    r"""
    Evaluates the sensitivity of the NURBS curve second derivative with respect to an individual control point at a given :math:`t`-value

    Parameters
    ----------
    w: Iterable[float]
        1-D list or array of weights corresponding to each of control points. Must have length
        equal to the outer dimension of ``p``.
    k: Iterable[float]
        1-D list or array of knots
    i: int
        Index of the control point
    q: int
        Degree of the curve
    dim: int
        Number of spatial dimensions in the curve. Usually ``2`` or ``3``
        1-D list or array of knots
    t: Iterable[float]
        Vector of parameter values

    Returns
    -------
    List[List[float]]
        Value of the NURBS curve second derivative sensitivity w.r.t. :math:`\mathbf{P}_i` along a vector of :math:`t`-values. Output array has size
        :math:`\text{len}(t) \times d`, where :math:`d` is the spatial dimension (usually ``3``)
    """

def nurbs_surf_eval(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], ku: Iterable[float], kv: Iterable[float], u: float, v: float) -> List[float]:
    r"""
    Evaluates a Non-Uniform Rational B-Spline (NURBS) surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair according to

    .. math::

        \mathbf{S}(u,v) = \frac{\sum_{i=0}^n \sum_{j=0}^m N_{i,q}(u) N_{j,r}(v) w_{i,j} \mathbf{P}_{i,j}}{\sum_{i=0}^n \sum_{j=0}^m N_{i,q}(u) N_{j,r}(v) w_{i,j}}

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. The degree of the B-spline
    in the :math:`u`-direction is computed as ``q = len(ku) - len(p) - 1``, and the degree of the B-spline
    surface in the :math:`v`-direction is computed as ``r = len(kv) - len(p[0]) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the NURBS surface at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def nurbs_surf_dsdu(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                    ku: Iterable[float], kv: Iterable[float], u: float, v: float) -> List[float]:
    r"""
    Evaluates the first derivative w.r.t. :math:`u` of a NURBS surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the NURBS surface first derivative w.r.t. :math:`u` at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def nurbs_surf_dsdv(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                    ku: Iterable[float], kv: Iterable[float], u: float, v: float) -> List[float]:
    r"""
    Evaluates the first derivative w.r.t. :math:`v` of a NURBS surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the NURBS surface first derivative w.r.t. :math:`v` at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def nurbs_surf_d2sdu2(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                      ku: Iterable[float], kv: Iterable[float], u: float, v: float) -> List[float]:
    r"""
    Evaluates the second derivative w.r.t. :math:`u` of a NURBS surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the NURBS surface second derivative w.r.t. :math:`u` at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def nurbs_surf_d2sdv2(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                      ku: Iterable[float], kv: Iterable[float], u: float, v: float) -> List[float]:
    r"""
    Evaluates the second derivative w.r.t. :math:`v` of a NURBS surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at a :math:`(u,v)` parameter pair
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction at which to evaluate the surface
    v: float
        Parameter value in the :math:`v`-direction at which to evaluate the surface

    Returns
    -------
    List[float]
        Value of the NURBS surface second derivative w.r.t. :math:`v` at :math:`(u,v)`. Has the same size as the innermost dimension of ``p``
    """

def nurbs_surf_eval_iso_u(p: Iterable[Iterable[Iterable[float]]],  w: Iterable[Iterable[float]],
                          ku: Iterable[float], kv: Iterable[float], u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates an isoparametric curve in :math:`u` of a NURBS surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` points along the :math:`u`-isoparametric curve of the NURBS surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_surf_eval_iso_v(p: Iterable[Iterable[Iterable[float]]],  w: Iterable[Iterable[float]],
                          ku: Iterable[float], kv: Iterable[float], nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates an isoparametric curve in :math:`v` of a NURBS surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` points along the :math:`v`-isoparametric curve of the NURBS surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_surf_dsdu_iso_u(p: Iterable[Iterable[Iterable[float]]],  w: Iterable[Iterable[float]],
                          ku: Iterable[float], kv: Iterable[float], u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the first derivative w.r.t. :math:`u` along an isoparametric curve in :math:`u` of a NURBS 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` first derivatives w.r.t. :math:`u` along the :math:`u`-isoparametric curve of the NURBS surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_surf_dsdu_iso_v(p: Iterable[Iterable[Iterable[float]]],  w: Iterable[Iterable[float]],
                          ku: Iterable[float], kv: Iterable[float], nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the first derivative w.r.t. :math:`u` along an isoparametric curve in :math:`v` of a NURBS 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` first derivatives w.r.t. :math:`u` along the :math:`v`-isoparametric curve of the NURBS surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_surf_dsdv_iso_u(p: Iterable[Iterable[Iterable[float]]],  w: Iterable[Iterable[float]],
                          ku: Iterable[float], kv: Iterable[float], u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the first derivative w.r.t. :math:`v` along an isoparametric curve in :math:`u` of a NURBS 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` first derivatives w.r.t. :math:`v` along the :math:`u`-isoparametric curve of the NURBS surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_surf_dsdv_iso_v(p: Iterable[Iterable[Iterable[float]]],  w: Iterable[Iterable[float]],
                          ku: Iterable[float], kv: Iterable[float], nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the first derivative w.r.t. :math:`v` along an isoparametric curve in :math:`v` of a NURBS 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` first derivatives w.r.t. :math:`v` along the :math:`v`-isoparametric curve of the NURBS surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_surf_d2sdu2_iso_u(p: Iterable[Iterable[Iterable[float]]],  w: Iterable[Iterable[float]],
                          ku: Iterable[float], kv: Iterable[float], u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`u` along an isoparametric curve in :math:`u` of a NURBS 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` second derivatives w.r.t. :math:`u` along the :math:`u`-isoparametric curve of the NURBS surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_surf_d2sdu2_iso_v(p: Iterable[Iterable[Iterable[float]]],  w: Iterable[Iterable[float]],
                          ku: Iterable[float], kv: Iterable[float], nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`u` along an isoparametric curve in :math:`v` of a NURBS 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` second derivatives w.r.t. :math:`u` along the :math:`v`-isoparametric curve of the NURBS surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_surf_d2sdv2_iso_u(p: Iterable[Iterable[Iterable[float]]],  w: Iterable[Iterable[float]],
                          ku: Iterable[float], kv: Iterable[float], u: float, nv: int) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`v` along an isoparametric curve in :math:`u` of a NURBS 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: float
        Parameter value in the :math:`u`-direction defining the isoparametric curve
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[float]]
        Values of :math:`N_v` second derivatives w.r.t. :math:`v` along the :math:`u`-isoparametric curve of the NURBS surface.
        Output array has size :math:`N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_surf_d2sdv2_iso_v(p: Iterable[Iterable[Iterable[float]]],  w: Iterable[Iterable[float]],
                          ku: Iterable[float], kv: Iterable[float], nu: int, v: float) -> List[List[float]]:
    r"""
    Evaluates the second derivative w.r.t. :math:`v` along an isoparametric curve in :math:`v` of a NURBS 
    surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_v` linearly-spaced points 
    along the :math:`v`-direction

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    v: float
        Parameter value in the :math:`v`-direction defining the isoparametric curve

    Returns
    -------
    List[List[float]]
        Values of :math:`N_u` second derivatives w.r.t. :math:`v` along the :math:`v`-isoparametric curve of the NURBS surface.
        Output array has size :math:`N_u \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_surf_eval_grid(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                         ku: Iterable[float], kv: Iterable[float], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates a Non-Uniform Rational B-Spline (NURBS) surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` 
    points along a linearly-spaced rectangular grid in :math:`(u,v)`-space according to

    .. math::

        \mathbf{S}(u,v) = \frac{\sum_{i=0}^n \sum_{j=0}^m N_{i,q}(u) N_{j,r}(v) w_{i,j} \mathbf{P}_{i,j}}{\sum_{i=0}^n \sum_{j=0}^m N_{i,q}(u) N_{j,r}(v) w_{i,j}}

    where :math:`N_{i,q}(t)` is the B-spline basis function of degree :math:`q`. The degree of the B-spline
    in the :math:`u`-direction is computed as ``q = len(ku) - len(p) - 1``, and the degree of the B-spline
    surface in the :math:`v`-direction is computed as ``r = len(kv) - len(p[0]) - 1``.

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` points on the NURBS surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_surf_dsdu_grid(p: Iterable[Iterable[Iterable[float]]],  w: Iterable[Iterable[float]], 
                         ku: Iterable[float], kv: Iterable[float], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`u` on a NURBS surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`u` on the NURBS surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def nurbs_surf_dsdv_grid(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                         ku: Iterable[float], kv: Iterable[float], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`v` on a NURBS surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`v` on the NURBS surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def nurbs_surf_d2sdu2_grid(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                           ku: Iterable[float], kv: Iterable[float], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`u` on a NURBS surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`u` on the NURBS surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def nurbs_surf_d2sdv2_grid(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                           ku: Iterable[float], kv: Iterable[float], nu: int, nv: int) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`v` on a NURBS surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at :math:`N_u \times N_v` points 
    along a linearly-spaced rectangular grid in :math:`(u,v)`-space

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    nu: int
        Number of linearly-spaced points in the :math:`u`-direction. E.g., ``nu=3`` outputs
        the evaluation of the surface at :math:`u=0.0`, :math:`u=0.5`, and :math:`u=1.0`.
    nv: int
        Number of linearly-spaced points in the :math:`v`-direction. E.g., ``nv=3`` outputs
        the evaluation of the surface at :math:`v=0.0`, :math:`v=0.5`, and :math:`v=1.0`.

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`v` on the NURBS surface at :math:`(u,v)`.
        Output array has size :math:`N_u \times N_v \times d`, where :math:`d` is the spatial dimension
        (usually either ``2``, ``3``, or ``4``)
    """

def nurbs_surf_eval_uvvecs(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                           ku: Iterable[float], kv: Iterable[float], u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates a NURBS surface with :math:`n+1` control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of points on the NURBS surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_surf_dsdu_uvvecs(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                           ku: Iterable[float], kv: Iterable[float], u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`u` on a NURBS surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`u` on the NURBS surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_surf_dsdv_uvvecs(p: Iterable[Iterable[Iterable[float]]], w: Iterable[Iterable[float]], 
                           ku: Iterable[float], kv: Iterable[float], u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the first derivative with respect to :math:`v` on a NURBS surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` first derivatives with respsect to :math:`v` on the NURBS surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_surf_d2sdu2_uvvecs(p: Iterable[Iterable[Iterable[float]]],  w: Iterable[Iterable[float]], 
                             ku: Iterable[float], kv: Iterable[float],u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`u` on a NURBS surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs
    
    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`u` on the NURBS surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """

def nurbs_surf_d2sdv2_uvvecs(p: Iterable[Iterable[Iterable[float]]],  w: Iterable[Iterable[float]], 
                             ku: Iterable[float], kv: Iterable[float],u: Iterable[float], v: Iterable[float]) -> List[List[List[float]]]:
    r"""
    Evaluates the second derivative with respect to :math:`v` on a NURBS surface with :math:`n+1` 
    control points in the :math:`u`-direction
    and :math:`m+1` control points in the :math:`v`-direction at any number of :math:`(u,v)` pairs

    Parameters
    ----------
    p: Iterable[Iterable[Iterable[float]]]
        3-D list or array of control points where the innermost dimension can have any size, but the typical
        size is ``3`` (:math:`x`-:math:`y`-:math:`z` space)
    w: Iterable[Iterable[float]]
        2-D list or array of weights corresponding to each of control points. The size of the array must be
        equal to the size of the first two dimensions of ``p`` (:math:`n+1 \times m+1`)
    ku: Iterable[float]
        1-D list or array of knots in the :math:`u`-parametric direction
    kv: Iterable[float]
        1-D list or array of knots in the :math:`v`-parametric direction
    u: Iterable[float]
        Vector of :math:`u`-values at which to evaluate the surface
    v: Iterable[float]
        Vector of :math:`v`-values at which to evaluate the surface

    Returns
    -------
    List[List[List[float]]]
        Values of :math:`N_u \times N_v` second derivatives with respsect to :math:`v` on the NURBS surface at each of the :math:`(u,v)` pairs.
        Output array has size :math:`\text{len}(u) \times \text{len}(v) \times d`, where :math:`d` is the spatial dimension
        (usually ``3``)
    """
