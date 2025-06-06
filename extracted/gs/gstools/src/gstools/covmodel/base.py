"""
GStools subpackage providing the base class for covariance models.

.. currentmodule:: gstools.covmodel.base

The following classes are provided

.. autosummary::
   CovModel
   SumModel
"""

# pylint: disable=C0103, R0201, E1101, C0302, W0613, W0231
import copy

import numpy as np
from hankel import SymmetricFourierTransform as SFT
from scipy.integrate import quad as integral

from gstools.covmodel import plot
from gstools.covmodel.fit import fit_variogram
from gstools.covmodel.sum_tools import (
    default_mod_kwargs,
    sum_check,
    sum_compare,
    sum_default_arg_bounds,
    sum_default_opt_arg_bounds,
    sum_model_repr,
    sum_set_len_weights,
    sum_set_var_weights,
)
from gstools.covmodel.tools import (
    _init_subclass,
    check_arg_bounds,
    check_arg_in_bounds,
    compare,
    default_arg_from_bounds,
    model_repr,
    percentile_scale,
    set_arg_bounds,
    set_dim,
    set_len_anis,
    set_model_angles,
    set_opt_args,
    spectral_rad_pdf,
)
from gstools.tools import RADIAN_SCALE
from gstools.tools.geometric import (
    great_circle_to_chordal,
    latlon2pos,
    matrix_anisometrize,
    matrix_isometrize,
    pos2latlon,
    rotated_main_axes,
)

__all__ = ["CovModel"]

# default arguments for hankel.SymmetricFourierTransform
HANKEL_DEFAULT = {"a": -1, "b": 1, "N": 200, "h": 0.001, "alt": True}


class CovModel:
    r"""Base class for the GSTools covariance models.

    Parameters
    ----------
    dim : :class:`int`, optional
        dimension of the model.
        Includes the temporal dimension if temporal is true.
        To specify only the spatial dimension in that case, use `spatial_dim`.
        Default: ``3``
    var : :class:`float`, optional
        variance of the model (the nugget is not included in "this" variance)
        Default: ``1.0``
    len_scale : :class:`float` or :class:`list`, optional
        length scale of the model.
        If a single value is given, the same length-scale will be used for
        every direction. If multiple values (for main and transversal
        directions) are given, `anis` will be
        recalculated accordingly. If only two values are given in 3D,
        the latter one will be used for both transversal directions.
        Default: ``1.0``
    nugget : :class:`float`, optional
        nugget of the model. Default: ``0.0``
    anis : :class:`float` or :class:`list`, optional
        anisotropy ratios in the transversal directions [e_y, e_z].

            * e_y = l_y / l_x
            * e_z = l_z / l_x

        If only one value is given in 3D, e_y will be set to 1.
        This value will be ignored, if multiple len_scales are given.
        Default: ``1.0``
    angles : :class:`float` or :class:`list`, optional
        angles of rotation (given in rad):

            * in 2D: given as rotation around z-axis
            * in 3D: given by yaw, pitch, and roll (known as Tait–Bryan angles)

         Default: ``0.0``
    integral_scale : :class:`float` or :class:`list` or :any:`None`, optional
        If given, ``len_scale`` will be ignored and recalculated,
        so that the integral scale of the model matches the given one.
        Default: :any:`None`
    rescale : :class:`float` or :any:`None`, optional
        Optional rescaling factor to divide the length scale with.
        This could be used for unit conversion or rescaling the length scale
        to coincide with e.g. the integral scale.
        Will be set by each model individually.
        Default: :any:`None`
    latlon : :class:`bool`, optional
        Whether the model is describing 2D fields on earths surface described
        by latitude and longitude. When using this, the model will internally
        use the associated 'Yadrenko' model to represent a valid model.
        This means, the spatial distance :math:`r` will be replaced by
        :math:`2\sin(\alpha/2)`, where :math:`\alpha` is the great-circle
        distance, which is equal to the spatial distance of two points in 3D.
        As a consequence, `dim` will be set to `3` and anisotropy will be
        disabled. `geo_scale` can be set to e.g. earth's radius,
        to have a meaningful `len_scale` parameter.
        Default: False
    geo_scale : :class:`float`, optional
        Geographic unit scaling in case of latlon coordinates to get a
        meaningful length scale unit.
        By default, len_scale is assumed to be in radians with latlon=True.
        Can be set to :any:`KM_SCALE` to have len_scale in km or
        :any:`DEGREE_SCALE` to have len_scale in degrees.
        Default: :any:`RADIAN_SCALE`
    temporal : :class:`bool`, optional
        Create a metric spatio-temporal covariance model.
        Setting this to true will increase `dim` and `field_dim` by 1.
        `spatial_dim` will be `field_dim - 1`.
        The time-dimension is appended, meaning the pos tuple is (x,y,z,...,t).
        Default: False
    spatial_dim : :class:`int`, optional
        spatial dimension of the model.
        If given, the model dimension will be determined from this spatial dimension
        and the possible temporal dimension if temporal is ture.
        Default: None
    hankel_kw: :class:`dict` or :any:`None`, optional
        Modify the init-arguments of
        :any:`hankel.SymmetricFourierTransform`
        used for the spectrum calculation. Use with caution (Better: Don't!).
        ``None`` is equivalent to ``{"a": -1, "b": 1, "N": 1000, "h": 0.001}``.
        Default: :any:`None`
    **opt_arg
        Optional arguments are covered by these keyword arguments.
        If present, they are described in the section `Other Parameters`.
    """

    _add_doc = True
    """Flag to append the above doc-string about parameters to the model implementation."""

    def __init__(
        self,
        dim=3,
        var=1.0,
        len_scale=1.0,
        nugget=0.0,
        anis=1.0,
        angles=0.0,
        *,
        integral_scale=None,
        rescale=None,
        latlon=False,
        geo_scale=RADIAN_SCALE,
        temporal=False,
        spatial_dim=None,
        hankel_kw=None,
        **opt_arg,
    ):
        # assert, that we use a subclass
        # this is the case, if __init_subclass__ is called, which creates
        # the "variogram"... so we check for that
        if not hasattr(self, "variogram"):
            raise TypeError("Don't instantiate 'CovModel' directly!")

        # indicator for initialization status (True after __init__)
        self._init = False
        # prepare dim setting
        self._dim = None
        self._hankel_kw = None
        self._sft = None
        # prepare parameters (they are checked in dim setting)
        self._rescale = None
        self._len_scale = None
        self._anis = None
        self._angles = None
        # prepare parameters boundaries
        self._var_bounds = None
        self._len_scale_bounds = None
        self._nugget_bounds = None
        self._anis_bounds = None
        self._opt_arg_bounds = {}
        # Set latlon and temporal first
        self._latlon = bool(latlon)
        self._temporal = bool(temporal)
        self._geo_scale = abs(float(geo_scale))
        # SFT class will be created within dim.setter but needs hankel_kw
        self.hankel_kw = hankel_kw
        # using time increases model dimension given by "spatial_dim"
        self.dim = (
            dim if spatial_dim is None else spatial_dim + int(self.temporal)
        )

        # optional arguments for the variogram-model
        set_opt_args(self, opt_arg)

        # set standard boundaries for variance, len_scale, nugget and opt_arg
        bounds = self.default_arg_bounds()
        bounds.update(self.default_opt_arg_bounds())
        self.set_arg_bounds(check_args=False, **bounds)

        # set parameters
        self.rescale = rescale
        self._var = float(var)
        self._nugget = float(nugget)

        # set anisotropy and len_scale, disable anisotropy for latlon models
        if integral_scale is not None:
            len_scale = integral_scale
        self._len_scale, self._anis = set_len_anis(
            self.dim, len_scale, anis, self.latlon
        )
        self._angles = set_model_angles(
            self.dim, angles, self.latlon, self.temporal
        )

        if integral_scale is not None:
            self.integral_scale = integral_scale

        # final check for parameter bounds
        self.check_arg_bounds()
        # additional checks for the optional arguments (provided by user)
        self.check_opt_arg()
        # precision for printing
        self._prec = 3
        # initialized
        self._init = True

    # one of these functions needs to be overridden
    def __init_subclass__(cls):
        """Initialize gstools covariance model."""
        _init_subclass(cls)

        # modify the docstrings: class docstring gets attributes added
        if cls.__doc__ is None:
            cls.__doc__ = "User defined GSTools Covariance-Model."
        if cls._add_doc:
            cls.__doc__ += CovModel.__doc__[45:]
        # overridden functions get standard doc if no new doc was created
        ign = ["__", "variogram", "covariance", "cor"]
        for att, attr_cls in cls.__dict__.items():
            if any(att.startswith(i) for i in ign) or att not in dir(CovModel):
                continue
            attr_doc = getattr(CovModel, att).__doc__
            if attr_cls.__doc__ is None:
                attr_cls.__doc__ = attr_doc

    # special variogram functions

    def vario_axis(self, r, axis=0):
        r"""Variogram along axis of anisotropy."""
        if axis == 0:
            return self.variogram(r)
        return self.variogram(np.abs(r) / self.anis[axis - 1])

    def cov_axis(self, r, axis=0):
        r"""Covariance along axis of anisotropy."""
        if axis == 0:
            return self.covariance(r)
        return self.covariance(np.abs(r) / self.anis[axis - 1])

    def cor_axis(self, r, axis=0):
        r"""Correlation along axis of anisotropy."""
        if axis == 0:
            return self.correlation(r)
        return self.correlation(np.abs(r) / self.anis[axis - 1])

    def vario_yadrenko(self, zeta):
        r"""Yadrenko variogram for great-circle distance from latlon-pos."""
        return self.variogram(great_circle_to_chordal(zeta, self.geo_scale))

    def cov_yadrenko(self, zeta):
        r"""Yadrenko covariance for great-circle distance from latlon-pos."""
        return self.covariance(great_circle_to_chordal(zeta, self.geo_scale))

    def cor_yadrenko(self, zeta):
        r"""Yadrenko correlation for great-circle distance from latlon-pos."""
        return self.correlation(great_circle_to_chordal(zeta, self.geo_scale))

    def vario_spatial(self, pos):
        r"""Spatial variogram respecting anisotropy and rotation."""
        return self.variogram(self._get_iso_rad(pos))

    def cov_spatial(self, pos):
        r"""Spatial covariance respecting anisotropy and rotation."""
        return self.covariance(self._get_iso_rad(pos))

    def cor_spatial(self, pos):
        r"""Spatial correlation respecting anisotropy and rotation."""
        return self.correlation(self._get_iso_rad(pos))

    def vario_nugget(self, r):
        """Isotropic variogram of the model respecting the nugget at r=0."""
        r = np.asarray(np.abs(r), dtype=np.double)
        r_gz = np.logical_not(np.isclose(r, 0))
        res = np.empty_like(r, dtype=np.double)
        res[r_gz] = self.variogram(r[r_gz])
        res[np.logical_not(r_gz)] = 0.0
        return res

    def cov_nugget(self, r):
        """Isotropic covariance of the model respecting the nugget at r=0."""
        r = np.asarray(np.abs(r), dtype=np.double)
        r_gz = np.logical_not(np.isclose(r, 0))
        res = np.empty_like(r, dtype=np.double)
        res[r_gz] = self.covariance(r[r_gz])
        res[np.logical_not(r_gz)] = self.sill
        return res

    def plot(self, func="variogram", **kwargs):  # pragma: no cover
        """
        Plot a function of a the CovModel.

        Parameters
        ----------
        func : :class:`str`, optional
            Function to be plotted. Could be one of:

                * "variogram"
                * "covariance"
                * "correlation"
                * "vario_spatial"
                * "cov_spatial"
                * "cor_spatial"
                * "vario_yadrenko"
                * "cov_yadrenko"
                * "cor_yadrenko"
                * "vario_axis"
                * "cov_axis"
                * "cor_axis"
                * "spectrum"
                * "spectral_density"
                * "spectral_rad_pdf"

        **kwargs
            Keyword arguments forwarded to the plotting function
            `"plot_" + func` in :py:mod:`gstools.covmodel.plot`.

        See Also
        --------
        gstools.covmodel.plot
        """
        routine = getattr(plot, "plot_" + func)
        return routine(self, **kwargs)

    # pykrige functions

    def pykrige_vario(self, args=None, r=0):  # pragma: no cover
        """Isotropic variogram of the model for pykrige."""
        if self.latlon:
            return self.vario_yadrenko(np.deg2rad(r))
        return self.variogram(r)

    @property
    def pykrige_anis(self):
        """2D anisotropy ratio for pykrige."""
        if self.dim == 2:
            return 1 / self.anis[0]
        return 1.0  # pragma: no cover

    @property
    def pykrige_anis_y(self):
        """3D anisotropy ratio in y direction for pykrige."""
        if self.dim >= 2:
            return 1 / self.anis[0]
        return 1.0  # pragma: no cover

    @property
    def pykrige_anis_z(self):
        """3D anisotropy ratio in z direction for pykrige."""
        if self.dim == 3:
            return 1 / self.anis[1]
        return 1.0  # pragma: no cover

    @property
    def pykrige_angle(self):
        """2D rotation angle for pykrige."""
        if self.dim == 2:
            return self.angles[0] / np.pi * 180
        return 0.0  # pragma: no cover

    @property
    def pykrige_angle_z(self):
        """3D rotation angle around z for pykrige."""
        if self.dim >= 2:
            return self.angles[0] / np.pi * 180
        return 0.0  # pragma: no cover

    @property
    def pykrige_angle_y(self):
        """3D rotation angle around y for pykrige."""
        if self.dim == 3:
            return self.angles[1] / np.pi * 180
        return 0.0  # pragma: no cover

    @property
    def pykrige_angle_x(self):
        """3D rotation angle around x for pykrige."""
        if self.dim == 3:
            return self.angles[2] / np.pi * 180
        return 0.0  # pragma: no cover

    @property
    def pykrige_kwargs(self):
        """Keyword arguments for pykrige routines."""
        kwargs = {
            "variogram_model": "custom",
            "variogram_parameters": [],
            "variogram_function": self.pykrige_vario,
        }
        if self.dim == 1:
            add_kwargs = {}
        elif self.dim == 2:
            add_kwargs = {
                "anisotropy_scaling": self.pykrige_anis,
                "anisotropy_angle": self.pykrige_angle,
            }
        else:
            add_kwargs = {
                "anisotropy_scaling_y": self.pykrige_anis_y,
                "anisotropy_scaling_z": self.pykrige_anis_z,
                "anisotropy_angle_x": self.pykrige_angle_x,
                "anisotropy_angle_y": self.pykrige_angle_y,
                "anisotropy_angle_z": self.pykrige_angle_z,
            }
        kwargs.update(add_kwargs)
        return kwargs

    # methods for optional/default arguments (can be overridden)

    def default_opt_arg(self):
        """Provide default optional arguments by the user.

        Should be given as a dictionary when overridden.
        """
        return {
            opt: default_arg_from_bounds(bnd)
            for (opt, bnd) in self.default_opt_arg_bounds().items()
        }

    def default_opt_arg_bounds(self):
        """Provide default boundaries for optional arguments."""
        res = {}
        for opt in self.opt_arg:
            res[opt] = [-np.inf, np.inf]
        return res

    def check_opt_arg(self):
        """Run checks for the optional arguments.

        This is in addition to the bound-checks

        Notes
        -----
        * You can use this to raise a ValueError/warning
        * Any return value will be ignored
        * This method will only be run once, when the class is initialized
        """

    def check_dim(self, dim):
        """Check the given dimension."""
        return True

    def fix_dim(self):
        """Set a fix dimension for the model."""
        return None

    def default_rescale(self):
        """Provide default rescaling factor."""
        return 1.0

    # calculation of different scales

    def calc_integral_scale(self):
        """Calculate the integral scale of the isotrope model."""
        return integral(self.correlation, 0, np.inf)[0]

    def percentile_scale(self, per=0.9):
        """Calculate the percentile scale of the isotrope model.

        This is the distance, where the given percentile of the variance
        is reached by the variogram
        """
        return percentile_scale(self, per)

    # spectrum methods (can be overridden for speedup)

    @property
    def needs_fourier_transform(self):
        """
        Flag whether the model needs a fourier transform to calculate
        the spectral density from the covariance function or if
        it implements an analytical spectral density.
        """
        base_method = getattr(CovModel, "spectral_density")
        instance_method = getattr(self.__class__, "spectral_density")
        return base_method == instance_method

    def spectrum(self, k):
        r"""
        Spectrum of the covariance model.

        This is given by:

        .. math:: S(\mathbf{k}) = \left(\frac{1}{2\pi}\right)^n
           \int C(r) e^{i \mathbf{k}\cdot\mathbf{r}} d^n\mathbf{r}

        Internally, this is calculated by the hankel transformation:

        .. math:: S(k) = \left(\frac{1}{2\pi}\right)^n \cdot
           \frac{(2\pi)^{n/2}}{k^{n/2-1}}
           \int_0^\infty r^{n/2} C(r) J_{n/2-1}(kr) dr

        Where :math:`C(r)` is the covariance function of the model.

        Parameters
        ----------
        k : :class:`float`
            Radius of the phase: :math:`k=\left\Vert\mathbf{k}\right\Vert`
        """
        return self.spectral_density(k) * self.var

    def spectral_density(self, k):
        r"""
        Spectral density of the covariance model.

        This is given by:

        .. math:: \tilde{S}(k) = \frac{S(k)}{\sigma^2}

        Where :math:`S(k)` is the spectrum of the covariance model.

        Parameters
        ----------
        k : :class:`float`
            Radius of the phase: :math:`k=\left\Vert\mathbf{k}\right\Vert`
        """
        k = np.asarray(np.abs(k), dtype=np.double)
        return self._sft.transform(self.correlation, k, ret_err=False)

    def spectral_rad_pdf(self, r):
        """Radial spectral density of the model."""
        return spectral_rad_pdf(self, r)

    def ln_spectral_rad_pdf(self, r):
        """Log radial spectral density of the model."""
        with np.errstate(divide="ignore"):
            return np.log(self.spectral_rad_pdf(r))

    def _has_cdf(self):
        """State if a cdf is defined with 'spectral_rad_cdf'."""
        return hasattr(self, "spectral_rad_cdf")

    def _has_ppf(self):
        """State if a ppf is defined with 'spectral_rad_ppf'."""
        return hasattr(self, "spectral_rad_ppf")

    # spatial routines

    def isometrize(self, pos):
        """Make a position tuple ready for isotropic operations."""
        pos = np.asarray(pos, dtype=np.double).reshape((self.field_dim, -1))
        if self.latlon:
            return latlon2pos(
                pos,
                radius=self.geo_scale,
                temporal=self.temporal,
                time_scale=self.anis[-1],
            )
        return np.dot(matrix_isometrize(self.dim, self.angles, self.anis), pos)

    def anisometrize(self, pos):
        """Bring a position tuple into the anisotropic coordinate-system."""
        pos = np.asarray(pos, dtype=np.double).reshape((self.dim, -1))
        if self.latlon:
            return pos2latlon(
                pos,
                radius=self.geo_scale,
                temporal=self.temporal,
                time_scale=self.anis[-1],
            )
        return np.dot(
            matrix_anisometrize(self.dim, self.angles, self.anis), pos
        )

    def main_axes(self):
        """Axes of the rotated coordinate-system."""
        return rotated_main_axes(self.dim, self.angles)

    def _get_iso_rad(self, pos):
        """Isometrized radians."""
        pos = np.asarray(pos, dtype=np.double).reshape((self.dim, -1))
        iso = np.dot(matrix_isometrize(self.dim, self.angles, self.anis), pos)
        return np.linalg.norm(iso, axis=0)

    # fitting routine

    def fit_variogram(
        self,
        x_data,
        y_data,
        anis=True,
        sill=None,
        init_guess="default",
        weights=None,
        method="trf",
        loss="soft_l1",
        max_eval=None,
        return_r2=False,
        curve_fit_kwargs=None,
        **para_select,
    ):
        """
        Fitting the variogram-model to an empirical variogram.

        Parameters
        ----------
        x_data : :class:`numpy.ndarray`
            The bin-centers of the empirical variogram.
        y_data : :class:`numpy.ndarray`
            The measured variogram
            If multiple are given, they are interpreted as the directional
            variograms along the main axis of the associated rotated
            coordinate system.
            Anisotropy ratios will be estimated in that case.
        anis : :class:`bool`, optional
            In case of a directional variogram, you can control anisotropy
            by this argument. Deselect the parameter from fitting, by setting
            it "False".
            You could also pass a fixed value to be set in the model.
            Then the anisotropy ratios wont be altered during fitting.
            Default: True
        sill : :class:`float` or :class:`bool`, optional
            Here you can provide a fixed sill for the variogram.
            It needs to be in a fitting range for the var and nugget bounds.
            If variance or nugget are not selected for estimation,
            the nugget will be recalculated to fulfill:

                * sill = var + nugget
                * if the variance is bigger than the sill,
                  nugget will bet set to its lower bound
                  and the variance will be set to the fitting partial sill.

            If variance is deselected, it needs to be less than the sill,
            otherwise a ValueError comes up. Same for nugget.
            If sill=False, it will be deselected from estimation
            and set to the current sill of the model.
            Then, the procedure above is applied.
            Default: None
        init_guess : :class:`str` or :class:`dict`, optional
            Initial guess for the estimation. Either:

                * "default": using the default values of the covariance model
                  ("len_scale" will be mean of given bin centers;
                  "var" and "nugget" will be mean of given variogram values
                  (if in given bounds))
                * "current": using the current values of the covariance model
                * dict: dictionary with parameter names and given value
                  (separate "default" can bet set to "default" or "current" for
                  unspecified values to get same behavior as given above
                  ("default" by default))
                  Example: ``{"len_scale": 10, "default": "current"}``

            Default: "default"
        weights : :class:`str`, :class:`numpy.ndarray`, :class:`callable`, optional
            Weights applied to each point in the estimation. Either:

                * 'inv': inverse distance ``1 / (x_data + 1)``
                * list: weights given per bin
                * callable: function applied to x_data

            If callable, it must take a 1-d ndarray.
            Then ``weights = f(x_data)``.
            Default: None
        method : {'trf', 'dogbox'}, optional
            Algorithm to perform minimization.

                * 'trf' : Trust Region Reflective algorithm,
                  particularly suitable for large sparse problems with bounds.
                  Generally robust method.
                * 'dogbox' : dogleg algorithm with rectangular trust regions,
                  typical use case is small problems with bounds.
                  Not recommended for problems with rank-deficient Jacobian.

            Default: 'trf'
        loss : :class:`str` or :class:`callable`, optional
            Determines the loss function in scipys curve_fit.
            The following keyword values are allowed:

                * 'linear' (default) : ``rho(z) = z``. Gives a standard
                  least-squares problem.
                * 'soft_l1' : ``rho(z) = 2 * ((1 + z)**0.5 - 1)``. The smooth
                  approximation of l1 (absolute value) loss. Usually a good
                  choice for robust least squares.
                * 'huber' : ``rho(z) = z if z <= 1 else 2*z**0.5 - 1``. Works
                  similarly to 'soft_l1'.
                * 'cauchy' : ``rho(z) = ln(1 + z)``. Severely weakens outliers
                  influence, but may cause difficulties in optimization process.
                * 'arctan' : ``rho(z) = arctan(z)``. Limits a maximum loss on
                  a single residual, has properties similar to 'cauchy'.

            If callable, it must take a 1-d ndarray ``z=f**2`` and return an
            array_like with shape (3, m) where row 0 contains function values,
            row 1 contains first derivatives and row 2 contains second
            derivatives. Default: 'soft_l1'
        max_eval : :class:`int` or :any:`None`, optional
            Maximum number of function evaluations before the termination.
            If None (default), the value is chosen automatically: 100 * n.
        return_r2 : :class:`bool`, optional
            Whether to return the r2 score of the estimation.
            Default: False
        curve_fit_kwargs : :class:`dict`, optional
            Other keyword arguments passed to scipys curve_fit. Default: None
        **para_select
            You can deselect parameters from fitting, by setting
            them "False" using their names as keywords.
            You could also pass fixed values for each parameter.
            Then these values will be applied and the involved parameters wont
            be fitted.
            By default, all parameters are fitted.

        Returns
        -------
        fit_para : :class:`dict`
            Dictionary with the fitted parameter values
        pcov : :class:`numpy.ndarray`
            The estimated covariance of `popt` from
            :any:`scipy.optimize.curve_fit`.
            To compute one standard deviation errors
            on the parameters use ``perr = np.sqrt(np.diag(pcov))``.
        r2_score : :class:`float`, optional
            r2 score of the curve fitting results. Only if return_r2 is True.

        Notes
        -----
        You can set the bounds for each parameter by accessing
        :any:`CovModel.set_arg_bounds`.

        The fitted parameters will be instantly set in the model.
        """
        return fit_variogram(
            model=self,
            x_data=x_data,
            y_data=y_data,
            anis=anis,
            sill=sill,
            init_guess=init_guess,
            weights=weights,
            method=method,
            loss=loss,
            max_eval=max_eval,
            return_r2=return_r2,
            curve_fit_kwargs=curve_fit_kwargs,
            **para_select,
        )

    # bounds setting and checks

    def default_arg_bounds(self):
        """Provide default boundaries for arguments.

        Given as a dictionary.
        """
        res = {
            "var": (0.0, np.inf, "co"),
            "len_scale": (0.0, np.inf, "co"),
            "nugget": (0.0, np.inf, "co"),
            "anis": (0.0, np.inf, "oo"),
        }
        return res

    def set_arg_bounds(self, check_args=True, **kwargs):
        r"""Set bounds for the parameters of the model.

        Parameters
        ----------
        check_args : bool, optional
            Whether to check if the arguments are in their valid bounds.
            In case not, a proper default value will be determined.
            Default: True
        **kwargs
            Parameter name as keyword ("var", "len_scale", "nugget", <opt_arg>)
            and a list of 2 or 3 values: ``[a, b]`` or ``[a, b, <type>]`` where
            <type> is one of ``"oo"``, ``"cc"``, ``"oc"`` or ``"co"``
            to define if the bounds are open ("o") or closed ("c").
        """
        return set_arg_bounds(self, check_args, **kwargs)

    def check_arg_bounds(self):
        """Check arguments to be within their given bounds."""
        return check_arg_bounds(self)

    # bounds properties

    @property
    def var_bounds(self):
        """:class:`list`: Bounds for the variance.

        Notes
        -----
        Is a list of 2 or 3 values: ``[a, b]`` or ``[a, b, <type>]`` where
        <type> is one of ``"oo"``, ``"cc"``, ``"oc"`` or ``"co"``
        to define if the bounds are open ("o") or closed ("c").
        """
        return self._var_bounds

    @var_bounds.setter
    def var_bounds(self, bounds):
        self.set_arg_bounds(var=bounds)

    @property
    def len_scale_bounds(self):
        """:class:`list`: Bounds for the length scale.

        Notes
        -----
        Is a list of 2 or 3 values: ``[a, b]`` or ``[a, b, <type>]`` where
        <type> is one of ``"oo"``, ``"cc"``, ``"oc"`` or ``"co"``
        to define if the bounds are open ("o") or closed ("c").
        """
        return self._len_scale_bounds

    @len_scale_bounds.setter
    def len_scale_bounds(self, bounds):
        self.set_arg_bounds(len_scale=bounds)

    @property
    def nugget_bounds(self):
        """:class:`list`: Bounds for the nugget.

        Notes
        -----
        Is a list of 2 or 3 values: ``[a, b]`` or ``[a, b, <type>]`` where
        <type> is one of ``"oo"``, ``"cc"``, ``"oc"`` or ``"co"``
        to define if the bounds are open ("o") or closed ("c").
        """
        return self._nugget_bounds

    @nugget_bounds.setter
    def nugget_bounds(self, bounds):
        self.set_arg_bounds(nugget=bounds)

    @property
    def anis_bounds(self):
        """:class:`list`: Bounds for the nugget.

        Notes
        -----
        Is a list of 2 or 3 values: ``[a, b]`` or ``[a, b, <type>]`` where
        <type> is one of ``"oo"``, ``"cc"``, ``"oc"`` or ``"co"``
        to define if the bounds are open ("o") or closed ("c").
        """
        return self._anis_bounds

    @anis_bounds.setter
    def anis_bounds(self, bounds):
        self.set_arg_bounds(anis=bounds)

    @property
    def opt_arg_bounds(self):
        """:class:`dict`: Bounds for the optional arguments.

        Notes
        -----
        Keys are the opt-arg names and values are lists of 2 or 3 values:
        ``[a, b]`` or ``[a, b, <type>]`` where
        <type> is one of ``"oo"``, ``"cc"``, ``"oc"`` or ``"co"``
        to define if the bounds are open ("o") or closed ("c").
        """
        return self._opt_arg_bounds

    @property
    def arg_bounds(self):
        """:class:`dict`: Bounds for all parameters.

        Notes
        -----
        Keys are the arg names and values are lists of 2 or 3 values:
        ``[a, b]`` or ``[a, b, <type>]`` where
        <type> is one of ``"oo"``, ``"cc"``, ``"oc"`` or ``"co"``
        to define if the bounds are open ("o") or closed ("c").
        """
        res = {
            "var": self.var_bounds,
            "len_scale": self.len_scale_bounds,
            "nugget": self.nugget_bounds,
            "anis": self.anis_bounds,
        }
        res.update(self.opt_arg_bounds)
        return res

    @property
    def temporal(self):
        """:class:`bool`: Whether the model is a metric spatio-temporal one."""
        return self._temporal

    # geographical coordinates related

    @property
    def latlon(self):
        """:class:`bool`: Whether the model depends on geographical coords."""
        return self._latlon

    @property
    def geo_scale(self):
        """:class:`float`: Geographic scaling for geographical coords."""
        return self._geo_scale

    @property
    def field_dim(self):
        """:class:`int`: The (parametric) field dimension of the model (with time)."""
        return 2 + int(self.temporal) if self.latlon else self.dim

    @property
    def spatial_dim(self):
        """:class:`int`: The spatial field dimension of the model (without time)."""
        return 2 if self.latlon else self.dim - int(self.temporal)

    # standard parameters

    @property
    def dim(self):
        """:class:`int`: The dimension of the model."""
        return self._dim

    @dim.setter
    def dim(self, dim):
        set_dim(self, dim)

    @property
    def var(self):
        """:class:`float`: The variance of the model."""
        return self._var

    @var.setter
    def var(self, var):
        self._var = float(var)
        self.check_arg_bounds()

    @property
    def nugget(self):
        """:class:`float`: The nugget of the model."""
        return self._nugget

    @nugget.setter
    def nugget(self, nugget):
        self._nugget = float(nugget)
        self.check_arg_bounds()

    @property
    def len_scale(self):
        """:class:`float`: The main length scale of the model."""
        return self._len_scale

    @len_scale.setter
    def len_scale(self, len_scale):
        self._len_scale, anis = set_len_anis(
            self.dim, len_scale, self.anis, self.latlon
        )
        self._anis = anis
        self.check_arg_bounds()

    @property
    def rescale(self):
        """:class:`float`: Rescale factor for the length scale of the model."""
        return self._rescale

    @rescale.setter
    def rescale(self, rescale):
        rescale = self.default_rescale() if rescale is None else rescale
        self._rescale = abs(float(rescale))

    @property
    def len_rescaled(self):
        """:class:`float`: The rescaled main length scale of the model."""
        return self.len_scale / self.rescale

    @property
    def anis(self):
        """:class:`numpy.ndarray`: The anisotropy factors of the model."""
        return self._anis

    @anis.setter
    def anis(self, anis):
        self._len_scale, self._anis = set_len_anis(
            self.dim, self.len_scale, anis, self.latlon
        )
        self.check_arg_bounds()

    @property
    def angles(self):
        """:class:`numpy.ndarray`: Rotation angles (in rad) of the model."""
        return self._angles

    @angles.setter
    def angles(self, angles):
        self._angles = set_model_angles(
            self.dim, angles, self.latlon, self.temporal
        )
        self.check_arg_bounds()

    @property
    def integral_scale(self):
        """:class:`float`: The main integral scale of the model.

        Raises
        ------
        ValueError
            If integral scale is not setable.
        """
        return self.calc_integral_scale()

    @integral_scale.setter
    def integral_scale(self, integral_scale):
        int_scale, anis = set_len_anis(
            self.dim, integral_scale, self.anis, self.latlon
        )
        old_scale = self.integral_scale
        self.anis = anis
        self.len_scale = self.len_scale * int_scale / old_scale
        if not np.isclose(self.integral_scale, int_scale, rtol=1e-3):
            raise ValueError(
                f"{self.name}: Integral scale could not be set correctly! "
                "Please just provide a 'len_scale'!"
            )

    @property
    def hankel_kw(self):
        """:class:`dict`: :any:`hankel.SymmetricFourierTransform` kwargs."""
        return self._hankel_kw

    @hankel_kw.setter
    def hankel_kw(self, hankel_kw):
        if self.needs_fourier_transform:
            if self._hankel_kw is None or hankel_kw is None:
                self._hankel_kw = copy.copy(HANKEL_DEFAULT)
            if hankel_kw is not None:
                self._hankel_kw.update(hankel_kw)
            if self.dim is not None:
                self._sft = SFT(ndim=self.dim, **self.hankel_kw)

    @property
    def dist_func(self):
        """:class:`tuple` of :any:`callable`: pdf, cdf and ppf.

        Spectral distribution info from the model.
        """
        pdf = self.spectral_rad_pdf
        cdf = None
        ppf = None
        if self.has_cdf:
            cdf = self.spectral_rad_cdf
        if self.has_ppf:
            ppf = self.spectral_rad_ppf
        return pdf, cdf, ppf

    @property
    def has_cdf(self):
        """:class:`bool`: State if a cdf is defined by the user."""
        return self._has_cdf()

    @property
    def has_ppf(self):
        """:class:`bool`: State if a ppf is defined by the user."""
        return self._has_ppf()

    @property
    def sill(self):
        """:class:`float`: The sill of the variogram.

        Notes
        -----
        This is calculated by:
            * ``sill = variance + nugget``
        """
        return self.var + self.nugget

    @property
    def arg(self):
        """:class:`list` of :class:`str`: Names of all arguments."""
        return ["var", "len_scale", "nugget", "anis", "angles"] + self.opt_arg

    @property
    def arg_list(self):
        """:class:`list` of :class:`float`: Values of all arguments."""
        alist = [self.var, self.len_scale, self.nugget, self.anis, self.angles]
        for opt in self.opt_arg:
            alist.append(getattr(self, opt))
        return alist

    @property
    def iso_arg(self):
        """:class:`list` of :class:`str`: Names of isotropic arguments."""
        return ["var", "len_scale", "nugget"] + self.opt_arg

    @property
    def iso_arg_list(self):
        """:class:`list` of :class:`float`: Values of isotropic arguments."""
        alist = [self.var, self.len_scale, self.nugget]
        for opt in self.opt_arg:
            alist.append(getattr(self, opt))
        return alist

    @property
    def opt_arg(self):
        """:class:`list` of :class:`str`: Names of the optional arguments."""
        return self._opt_arg

    @property
    def len_scale_vec(self):
        """:class:`numpy.ndarray`: The length scales in each direction.

        Notes
        -----
        This is calculated by:
            * ``len_scale_vec[0] = len_scale``
            * ``len_scale_vec[1] = len_scale*anis[0]``
            * ``len_scale_vec[2] = len_scale*anis[1]``
        """
        res = np.zeros(self.dim, dtype=np.double)
        res[0] = self.len_scale
        for i in range(1, self.dim):
            res[i] = self.len_scale * self.anis[i - 1]
        return res

    @property
    def integral_scale_vec(self):
        """:class:`numpy.ndarray`: The integral scales in each direction.

        Notes
        -----
        This is calculated by:
            * ``integral_scale_vec[0] = integral_scale``
            * ``integral_scale_vec[1] = integral_scale*anis[0]``
            * ``integral_scale_vec[2] = integral_scale*anis[1]``
        """
        res = np.zeros(self.dim, dtype=np.double)
        res[0] = self.integral_scale
        for i in range(1, self.dim):
            res[i] = self.integral_scale * self.anis[i - 1]
        return res

    @property
    def name(self):
        """:class:`str`: The name of the CovModel class."""
        return self.__class__.__name__

    @property
    def do_rotation(self):
        """:any:`bool`: State if a rotation is performed."""
        return not np.all(np.isclose(self.angles, 0.0))

    @property
    def is_isotropic(self):
        """:any:`bool`: State if a model is isotropic."""
        return np.all(np.isclose(self.anis, 1.0))

    def __eq__(self, other):
        """Compare CovModels."""
        if not isinstance(other, CovModel):
            return False
        if isinstance(other, SumModel):
            return False
        return compare(self, other)

    def __setattr__(self, name, value):
        """Set an attribute."""
        super().__setattr__(name, value)
        # if an optional variogram argument was given, check bounds
        if getattr(self, "_init", False) and name in self.opt_arg:
            self.check_arg_bounds()

    def __add__(self, other):
        """Add two covariance models and return a SumModel."""
        return SumModel(self, other)

    def __radd__(self, other):
        """Add two covariance models and return a SumModel."""
        return SumModel(self, other)

    def __repr__(self):
        """Return String representation."""
        return model_repr(self)


class SumModel(CovModel):
    r"""Class for sums of covariance models.

    This class represents sums of covariance models. The nugget of
    each contained model will be set to zero and the sum model will
    have its own nugget.
    The variance of the sum model is the sum of the sub model variances
    and the length scale of the sum model is the variance-weighted sum
    of the length scales of the sub models. This is motivated by the fact,
    that the integral scale of the sum model is equal to the variance-weighted
    sum of the integral scales of the sub models.
    An empty sum represents a pure Nugget model.
    Resetting the total variance or the total length scale will evenly
    scale the variances or length scales of the sub models.
    Sum models will have a constant rescale factor of one.

    Parameters
    ----------
    *models
        tuple of :any:`CovModel` instances or subclasses to sum.
        All models will get a nugget of zero and the nugget will
        be set in the SumModel directly.
        Models need to have matching temporal setting,
        latlon setting, anis, angles and geo_scale.
        The model dimension will be specified by the first given model.
    dim : :class:`int`, optional
        dimension of the model.
        Includes the temporal dimension if temporal is true.
        To specify only the spatial dimension in that case, use `spatial_dim`.
        Default: ``3`` or dimension of the first given model (if instance).
    vars : :class:`list` of :class:`float`, optional
        variances of the models. Will reset present variances.
    len_scales : :class:`list` of :class:`float`, optional
        length scale of the models. Will reset present length scales.
    nugget : :class:`float`, optional
        nugget of the sum-model. All summed models will have a nugget of zero.
        Default: ``0.0``
    anis : :class:`float` or :class:`list`, optional
        anisotropy ratios in the transversal directions [e_y, e_z].

            * e_y = l_y / l_x
            * e_z = l_z / l_x

        If only one value is given in 3D, e_y will be set to 1.
        This value will be ignored, if multiple len_scales are given.
        Default: ``1.0`` or anis of the first given model (if instance).
    angles : :class:`float` or :class:`list`, optional
        angles of rotation (given in rad):

            * in 2D: given as rotation around z-axis
            * in 3D: given by yaw, pitch, and roll (known as Tait–Bryan angles)

         Default: ``0.0`` or angles of the first given model (if instance).
    integral_scale : :class:`float` or :class:`list` or :any:`None`, optional
        If given, ``len_scale`` will be ignored and recalculated,
        so that the integral scale of the model matches the given one.
        Default: :any:`None`
    latlon : :class:`bool`, optional
        Whether the model is describing 2D fields on earths surface described
        by latitude and longitude. When using this, the model will internally
        use the associated 'Yadrenko' model to represent a valid model.
        This means, the spatial distance :math:`r` will be replaced by
        :math:`2\sin(\alpha/2)`, where :math:`\alpha` is the great-circle
        distance, which is equal to the spatial distance of two points in 3D.
        As a consequence, `dim` will be set to `3` and anisotropy will be
        disabled. `geo_scale` can be set to e.g. earth's radius,
        to have a meaningful `len_scale` parameter.
        Default: False or latlon config of the first given model (if instance).
    geo_scale : :class:`float`, optional
        Geographic unit scaling in case of latlon coordinates to get a
        meaningful length scale unit.
        By default, len_scale is assumed to be in radians with latlon=True.
        Can be set to :any:`KM_SCALE` to have len_scale in km or
        :any:`DEGREE_SCALE` to have len_scale in degrees.
        Default: :any:`RADIAN_SCALE` or geo_scale of the first given model (if instance).
    temporal : :class:`bool`, optional
        Create a metric spatio-temporal covariance model.
        Setting this to true will increase `dim` and `field_dim` by 1.
        `spatial_dim` will be `field_dim - 1`.
        The time-dimension is appended, meaning the pos tuple is (x,y,z,...,t).
        Default: False or temporal config of the first given model (if instance).
    spatial_dim : :class:`int`, optional
        spatial dimension of the model.
        If given, the model dimension will be determined from this spatial dimension
        and the possible temporal dimension if temporal is ture.
        Default: None
    var : :class:`float`, optional
        Total variance of the sum-model. Will evenly scale present variances.
    len_scale : :class:`float` or :class:`list`, optional
        Total length scale of the sum-model. Will evenly scale present length scales.
    **opt_arg
        Optional arguments of the sub-models will have and added index of the sub-model.
        Also covers ``var_<i>`` and ``length_scale_<i>`` but they should preferably be
        set by ``vars`` and ``length_scales``.
    """

    _add_doc = False

    def __init__(self, *models, **kwargs):
        self._init = False
        self._models = []
        add_nug = 0.0
        to_init = None
        imsg = (
            "SumModel: either all models are CovModel instances or subclasses."
        )
        for mod in models:
            if isinstance(mod, type) and issubclass(mod, SumModel):
                if to_init is not None and not to_init:
                    raise ValueError(imsg)
                to_init = True
                continue  # treat un-init sum-model as nugget model with 0 nugget
            if isinstance(mod, SumModel):
                if to_init is not None and to_init:
                    raise ValueError(imsg)
                to_init = False
                self._models += copy.deepcopy(mod.models)
                add_nug += mod.nugget
            elif isinstance(mod, CovModel):
                if to_init is not None and to_init:
                    raise ValueError(imsg)
                to_init = False
                self._models.append(copy.deepcopy(mod))
            elif isinstance(mod, type) and issubclass(mod, CovModel):
                if to_init is not None and not to_init:
                    raise ValueError(imsg)
                to_init = True
                self._models.append(mod(**default_mod_kwargs(kwargs)))
            else:
                msg = "SumModel: models need to be instances or subclasses of CovModel."
                raise ValueError(msg)
        # handle parameters when only Nugget models given
        if models and not self.models:
            for mod in models:
                if not isinstance(mod, type):
                    kwargs.setdefault("dim", mod.dim)
                    kwargs.setdefault("latlon", mod.latlon)
                    kwargs.setdefault("temporal", mod.temporal)
                    kwargs.setdefault("geo_scale", mod.geo_scale)
                    kwargs.setdefault("anis", mod.anis)
                    kwargs.setdefault("angles", mod.angles)
                    break
        # pop entries that can't be re-set
        self._latlon = bool(
            kwargs.pop(
                "latlon", self.models[0].latlon if self.models else False
            )
        )
        self._temporal = bool(
            kwargs.pop(
                "temporal", self.models[0].temporal if self.models else False
            )
        )
        self._geo_scale = float(
            kwargs.pop(
                "geo_scale",
                self.models[0].geo_scale if self.models else RADIAN_SCALE,
            )
        )
        var_set = kwargs.pop("var", None)
        len_set = kwargs.pop("len_scale", None)
        # convert nugget
        self._nugget = float(
            kwargs.pop(
                "nugget",
                sum((mod.nugget for mod in self.models), 0) + add_nug,
            )
        )
        for mod in self.models:
            mod._nugget = 0.0
        # prepare dim setting
        if "spatial_dim" in kwargs:
            spatial_dim = kwargs.pop("spatial_dim")
            if spatial_dim is not None:
                kwargs["dim"] = spatial_dim + int(self.temporal)
        self._dim = None
        self._hankel_kw = None
        self._sft = None
        self.dim = kwargs.get("dim", self.models[0].dim if self.models else 3)
        # prepare parameters (they are checked in dim setting)
        anis = kwargs.get("anis", self.models[0].anis if self.models else 1)
        angles = kwargs.get(
            "angles", self.models[0].angles if self.models else 0
        )
        _, self._anis = set_len_anis(self.dim, 1.0, anis, self.latlon)
        self._angles = set_model_angles(
            self.dim, angles, self.latlon, self.temporal
        )
        # prepare parameter boundaries
        self._var_bounds = None
        self._len_scale_bounds = None
        self._nugget_bounds = None
        self._anis_bounds = None
        self._opt_arg_bounds = {}
        bounds = self.default_arg_bounds()
        bounds.update(self.default_opt_arg_bounds())
        self.set_arg_bounds(check_args=False, **bounds)
        # finalize init
        self._prec = 3
        self._init = True
        # set remaining args
        for arg, val in kwargs.items():
            setattr(self, arg, val)
        # reset total variance and length scale last
        if var_set is not None:
            self.var = var_set
        if len_set is not None:
            self.len_scale = len_set
        # check consistency of sub models
        self.check()

    def __iter__(self):
        return iter(self.models)

    def __len__(self):
        return self.size

    def __contains__(self, item):
        return item in self.models

    def __getitem__(self, key):
        return self.models[key]

    def check(self):
        """Check consistency of contained models."""
        sum_check(self)

    def default_arg_bounds(self):
        """Default boundaries for arguments as dict."""
        return sum_default_arg_bounds(self)

    def default_opt_arg_bounds(self):
        """Defaults boundaries for optional arguments as dict."""
        return sum_default_opt_arg_bounds(self)

    def set_var_weights(self, weights, skip=None, var=None):
        """
        Set variances of contained models by weights.

        The variances of the sub-models act as ratios for the sum-model.
        This function enables to keep the total variance of the sum-model
        and reset the individual variances of the contained sub-models
        by the given weights.

        Parameters
        ----------
        weights : iterable
            Weights to set. Should have a length of len(models) - len(skip)
        skip : iterable, optional
            Model indices to skip. Should have compatible length, by default None
        var : float, optional
            Desired variance, by default current variance

        Raises
        ------
        ValueError
            If number of weights is not matching.
        """
        sum_set_var_weights(self, weights, skip, var)

    def set_len_weights(self, weights, skip=None, len_scale=None):
        """
        Set length scales of contained models by weights.

        The variances of the sub-models act as ratios for the sub-model length
        scales to determine the total length scale of the sum-model.
        This function enables to keep the total length scale of the sum-model as
        well as the variances of the sub-models and reset the individual length scales
        of the contained sub-models by the given weights.

        Parameters
        ----------
        weights : iterable
            Weights to set. Should have a length of len(models) - len(skip)
        skip : iterable, optional
            Model indices to skip. Should have compatible length, by default None
        len_scale : float, optional
            Desired len_scale, by default current len_scale

        Raises
        ------
        ValueError
            If number of weights is not matching.
        """
        sum_set_len_weights(self, weights, skip, len_scale)

    @property
    def models(self):
        """:class:`tuple`: The summed models."""
        return self._models

    @property
    def size(self):
        """:class:`int`: Number of summed models."""
        return len(self._models)

    @property
    def rescale(self):
        """:class:`float`: SumModel has a constant rescale factor of one."""
        return 1.0

    @property
    def geo_scale(self):
        """:class:`float`: Geographic scaling for geographical coords."""
        return self._geo_scale

    @geo_scale.setter
    def geo_scale(self, geo_scale):
        self._geo_scale = abs(float(geo_scale))
        for mod in self.models:
            mod.geo_scale = geo_scale

    @property
    def dim(self):
        """:class:`int`: The dimension of the model."""
        return self._dim

    @dim.setter
    def dim(self, dim):
        set_dim(self, dim)
        for mod in self.models:
            mod.dim = dim

    @property
    def var(self):
        """:class:`float`: The variance of the model."""
        return sum((var for var in self.vars), 0.0)

    @var.setter
    def var(self, var):
        for mod, rat in zip(self.models, self.ratios):
            mod.var = rat * var
        if not self.models and not np.isclose(var, 0):
            msg = f"{self.name}: variance needs to be 0."
            raise ValueError(msg)
        check_arg_in_bounds(self, "var", error=True)
        check_arg_in_bounds(self, "len_scale", error=True)

    @property
    def vars(self):
        """:class:`list`: The variances of the models."""
        return [mod.var for mod in self.models]

    @vars.setter
    def vars(self, variances):
        if len(variances) != len(self):
            msg = "SumModel: number of given variances not matching"
            raise ValueError(msg)
        for mod, var in zip(self.models, variances):
            mod.var = var
        check_arg_in_bounds(self, "var", error=True)
        check_arg_in_bounds(self, "len_scale", error=True)

    @property
    def len_scale(self):
        """:class:`float`: The main length scale of the model."""
        return sum(
            (
                mod.len_scale * rat
                for mod, rat in zip(self.models, self.ratios)
            ),
            0.0,
        )

    @len_scale.setter
    def len_scale(self, len_scale):
        len_scale, anis = set_len_anis(
            self.dim, len_scale, self.anis, self.latlon
        )
        old_scale = self.len_scale
        self.anis = anis
        for mod in self.models:
            mod.len_scale = mod.len_scale * len_scale / old_scale
        if not self.models and not np.isclose(len_scale, 0):
            msg = f"{self.name}: length scale needs to be 0."
            raise ValueError(msg)
        check_arg_in_bounds(self, "len_scale", error=True)

    @property
    def len_scales(self):
        """:class:`list`: The main length scales of the models."""
        return [mod.len_scale for mod in self.models]

    @len_scales.setter
    def len_scales(self, len_scales):
        if len(len_scales) != len(self):
            msg = "SumModel: number of given length scales not matching"
            raise ValueError(msg)
        for mod, len_scale in zip(self.models, len_scales):
            mod.len_scale = len_scale
        check_arg_in_bounds(self, "len_scale", error=True)

    @property
    def anis(self):
        """:class:`numpy.ndarray`: The anisotropy factors of the model."""
        return self._anis

    @anis.setter
    def anis(self, anis):
        _, self._anis = set_len_anis(self.dim, 1.0, anis, self.latlon)
        for mod in self.models:
            mod.anis = anis
        check_arg_in_bounds(self, "anis", error=True)

    @property
    def angles(self):
        """:class:`numpy.ndarray`: Rotation angles (in rad) of the model."""
        return self._angles

    @angles.setter
    def angles(self, angles):
        self._angles = set_model_angles(
            self.dim, angles, self.latlon, self.temporal
        )
        for mod in self.models:
            mod.angles = angles

    @property
    def ratios(self):
        """:class:`numpy.ndarray`: Variance ratios of the sub-models."""
        var = self.var
        if np.isclose(var, 0) and len(self) > 0:
            return np.full(len(self), 1 / len(self))
        return np.array([mod.var / var for mod in self.models])

    @ratios.setter
    def ratios(self, ratios):
        if len(ratios) != len(self):
            msg = "SumModel.ratios: wrong number of given ratios."
            raise ValueError(msg)
        if ratios and not np.isclose(np.sum(ratios), 1):
            msg = "SumModel.ratios: given ratios do not sum to 1."
            raise ValueError(msg)
        var = self.var
        for mod, rat in zip(self.models, ratios):
            mod.var = var * rat
        check_arg_in_bounds(self, "var", error=True)
        check_arg_in_bounds(self, "len_scale", error=True)

    def calc_integral_scale(self):
        return sum(
            (
                mod.integral_scale * rat
                for mod, rat in zip(self.models, self.ratios)
            ),
            0.0,
        )

    @property
    def needs_fourier_transform(self):
        """Whether the model doesn't implement an analytical spectral density."""
        return False

    def spectral_density(self, k):
        return sum(
            (
                mod.spectral_density(k) * rat
                for mod, rat in zip(self.models, self.ratios)
            ),
            np.zeros_like(k, dtype=np.double),
        )

    def correlation(self, r):
        """SumModel correlation function."""
        return sum(
            (
                mod.correlation(r) * rat
                for mod, rat in zip(self.models, self.ratios)
            ),
            np.zeros_like(r, dtype=np.double),
        )

    @property
    def opt_arg(self):
        """:class:`list` of :class:`str`: Names of the optional arguments."""
        return sum(
            [
                [f"{opt}_{i}" for opt in mod.opt_arg]
                for i, mod in enumerate(self.models)
            ],
            [],
        )

    @property
    def sub_arg(self):
        """:class:`list` of :class:`str`: Names of the sub-arguments for var and len_scale."""
        return [
            f"{o}_{i}" for o in ["var", "len_scale"] for i in range(self.size)
        ]

    @property
    def sub_arg_bounds(self):
        """:class:`dict`: Names of the sub-arguments for var and len_scale."""
        return {
            f"{o}_{i}": mod.arg_bounds[o]
            for o in ["var", "len_scale"]
            for (i, mod) in enumerate(self.models)
        }

    @property
    def arg_bounds(self):
        """:class:`dict`: Bounds for all parameters.

        Notes
        -----
        Keys are the arg names and values are lists of 2 or 3 values:
        ``[a, b]`` or ``[a, b, <type>]`` where
        <type> is one of ``"oo"``, ``"cc"``, ``"oc"`` or ``"co"``
        to define if the bounds are open ("o") or closed ("c").
        """
        res = {
            "var": self.var_bounds,
            "len_scale": self.len_scale_bounds,
            "nugget": self.nugget_bounds,
            "anis": self.anis_bounds,
        }
        res.update(self.opt_arg_bounds)
        res.update(self.sub_arg_bounds)
        return res

    def __setattr__(self, name, value):
        """Set an attribute."""
        sub_arg = False
        if getattr(self, "_init", False):
            for i, mod in enumerate(self.models):
                if name == f"var_{i}":
                    mod.var = value
                    sub_arg = True
                if name == f"len_scale_{i}":
                    mod.len_scale = value
                    sub_arg = True
                if name == f"integral_scale_{i}":
                    mod.integral_scale = value
                    sub_arg = True
                for opt in mod.opt_arg:
                    if name == f"{opt}_{i}":
                        setattr(mod, opt, value)
                        sub_arg = True
                if sub_arg:
                    break
        if sub_arg:
            self.check_arg_bounds()
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        """Get an attribute."""
        # __getattr__ is only called when an attribute is not found in the usual places
        if name != "_init" and getattr(self, "_init", False):
            for i, mod in enumerate(self.models):
                if name == f"var_{i}":
                    return mod.var
                if name == f"len_scale_{i}":
                    return mod.len_scale
                if name == f"integral_scale_{i}":
                    return mod.integral_scale
                for opt in mod.opt_arg:
                    if name == f"{opt}_{i}":
                        return getattr(mod, opt)
        raise AttributeError(f"'{self.name}' object has no attribute '{name}'")

    def __eq__(self, other):
        """Compare SumModels."""
        if not isinstance(other, SumModel):
            return False
        return sum_compare(self, other)

    def __repr__(self):
        """Return String representation."""
        return sum_model_repr(self)
