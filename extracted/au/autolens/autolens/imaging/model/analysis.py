import logging
import numpy as np
from typing import Dict, Optional, Tuple

from autoconf.dictable import to_dict

import autofit as af
import autogalaxy as ag

from autoarray.exc import PixelizationException

from autolens.analysis.analysis.dataset import AnalysisDataset
from autolens.imaging.model.result import ResultImaging
from autolens.imaging.model.visualizer import VisualizerImaging
from autolens.imaging.fit_imaging import FitImaging

from autolens import exc

logger = logging.getLogger(__name__)

logger.setLevel(level="INFO")


class AnalysisImaging(AnalysisDataset):

    Result = ResultImaging
    Visualizer = VisualizerImaging

    def modify_before_fit(self, paths: af.DirectoryPaths, model: af.Collection):
        """
        This function is called immediately before the non-linear search begins and performs final tasks and checks 
        before it begins.

        This function:

        - Checks that the adapt-dataset is consistent with previous adapt-datasets if the model-fit is being
          resumed from a previous run.

        - Checks the model and raises exceptions if certain critieria are not met.

        Once inherited from it also visualizes objects which do not change throughout the model fit like the dataset.

        Parameters
        ----------
        paths
            The paths object which manages all paths, e.g. where the non-linear search outputs are stored,
            visualization and the pickled objects used by the aggregator output by this function.
        model
            The model object, which includes model components representing the galaxies that are fitted to
            the imaging data.
        """
        super().modify_before_fit(paths=paths, model=model)

        return self

    def log_likelihood_function(self, instance: af.ModelInstance) -> float:
        """
        Given an instance of the model, where the model parameters are set via a non-linear search, fit the model
        instance to the imaging dataset.

        This function returns a log likelihood which is used by the non-linear search to guide the model-fit.

        For this analysis class, this function performs the following steps:

        1) If the analysis has a adapt image, associated the model galaxy images of this dataset to the galaxies in
           the model instance.

        2) Extract attributes which model aspects of the data reductions, like the scaling the background sky
           and background noise.

        3) Extracts all galaxies from the model instance and set up a `Tracer`, which includes ordering the galaxies
           by redshift to set up each `Plane`.

        4) Use the `Tracer` and other attributes to create a `FitImaging` object, which performs steps such as creating
           model images of every galaxy in the tracer, blurring them with the imaging dataset's PSF and computing
           residuals, a chi-squared statistic and the log likelihood.

        Certain models will fail to fit the dataset and raise an exception. For example if an `Inversion` is used, the
        linear algebra calculation may be invalid and raise an Exception. In such circumstances the model is discarded
        and its likelihood value is passed to the non-linear search in a way that it ignores it (for example, using a
        value of -1.0e99).

        Parameters
        ----------
        instance
            An instance of the model that is being fitted to the data by this analysis (whose parameters have been set
            via a non-linear search).

        Returns
        -------
        float
            The log likelihood indicating how well this model instance fitted the imaging data.
        """

        try:
            log_likelihood_positions_overwrite = self.log_likelihood_positions_overwrite_from(
                instance=instance
            )
            if log_likelihood_positions_overwrite is not None:
                return log_likelihood_positions_overwrite
        except Exception as e:
            raise e

        if log_likelihood_positions_overwrite is not None:
            return log_likelihood_positions_overwrite

        try:
            return self.fit_from(instance=instance).figure_of_merit
        except (
            PixelizationException,
            exc.PixelizationException,
            exc.InversionException,
            exc.GridException,
            exc.MeshException,
            ValueError,
            TypeError,
            np.linalg.LinAlgError,
            OverflowError,
        ) as e:
            raise exc.FitException from e

    def fit_from(
        self,
        instance: af.ModelInstance,
        run_time_dict: Optional[Dict] = None,
    ) -> FitImaging:
        """
        Given a model instance create a `FitImaging` object.

        This function is used in the `log_likelihood_function` to fit the model to the imaging data and compute the
        log likelihood.

        Parameters
        ----------
        instance
            An instance of the model that is being fitted to the data by this analysis (whose parameters have been set
            via a non-linear search).
        check_positions
            Whether the multiple image positions of the lensed source should be checked, i.e. whether they trace
            within the position threshold of one another in the source plane.
        run_time_dict
            A dictionary which times functions called to fit the model to data, for profiling.

        Returns
        -------
        FitImaging
            The fit of the plane to the imaging dataset, which includes the log likelihood.
        """

        tracer = self.tracer_via_instance_from(
            instance=instance, run_time_dict=run_time_dict
        )

        dataset_model = self.dataset_model_via_instance_from(instance=instance)

        adapt_images = self.adapt_images_via_instance_from(instance=instance)

        return FitImaging(
            dataset=self.dataset,
            tracer=tracer,
            dataset_model=dataset_model,
            adapt_images=adapt_images,
            settings_inversion=self.settings_inversion,
            run_time_dict=run_time_dict,
        )

    def save_attributes(self, paths: af.DirectoryPaths):
        """
        Before the non-linear search begins, this routine saves attributes of the `Analysis` object to the `files`
        folder such that they can be loaded after the analysis using PyAutoFit's database and aggregator tools.


         For this analysis, it uses the `AnalysisDataset` object's method to output the following:

         - The settings associated with the inversion.
         - The settings associated with the pixelization.
         - The Cosmology.
         - The adapt image's model image and galaxy images, as `adapt_images.fits`, if used.

        This function also outputs attributes specific to lens modeling:

        - The positions of the brightest pixels in the lensed source which are used to discard mass models.

        The following .fits files are also output via the plotter interface:

        - The mask applied to the dataset, in the `PrimaryHDU` of `dataset.fits`.
        - The imaging dataset as `dataset.fits` (data / noise-map / psf / over sampler / etc.).

        It is common for these attributes to be loaded by many of the template aggregator functions given in the
        `aggregator` modules. For example, when using the database tools to perform a fit, the default behaviour is for
        the dataset, settings and other attributes necessary to perform the fit to be loaded via the pickle files
        output by this function.

        Parameters
        ----------
        paths
            The paths object which manages all paths, e.g. where the non-linear search outputs are stored,
            visualization, and the pickled objects used by the aggregator output by this function.
        """
        super().save_attributes(paths=paths)

        analysis = ag.AnalysisImaging(
            dataset=self.dataset,
        )

        analysis.save_attributes(paths=paths)

        if self.positions_likelihood is not None:

            paths.save_json(
                name="positions",
                object_dict=to_dict(self.positions_likelihood.positions),
                prefix="dataset",
            )

    def profile_log_likelihood_function(
        self, instance: af.ModelInstance, paths: Optional[af.DirectoryPaths] = None
    ) -> Tuple[Dict, Dict]:
        """
        This function is optionally called throughout a model-fit to profile the log likelihood function.

        All function calls inside the `log_likelihood_function` that are decorated with the `profile_func` are timed
        with their times stored in a dictionary called the `run_time_dict`.

        An `info_dict` is also created which stores information on aspects of the model and dataset that dictate
        run times, so the profiled times can be interpreted with this context.

        The results of this profiling are then output to hard-disk in the `profiling` folder of the model-fit results,
        which they can be inspected to ensure run-times are as expected.

        Parameters
        ----------
        instance
            An instance of the model that is being fitted to the data by this analysis (whose parameters have been set
            via a non-linear search).
        paths
            The paths object which manages all paths, e.g. where the non-linear search outputs are stored,
            visualization and the pickled objects used by the aggregator output by this function.

        Returns
        -------
        Two dictionaries, the profiling dictionary and info dictionary, which contain the profiling times of the
        `log_likelihood_function` and information on the model and dataset used to perform the profiling.
        """
        run_time_dict, info_dict = super().profile_log_likelihood_function(
            instance=instance,
        )

        info_dict["psf_shape_2d"] = self.dataset.psf.shape_native

        self.output_profiling_info(paths=paths, run_time_dict=run_time_dict, info_dict=info_dict)

        return run_time_dict, info_dict