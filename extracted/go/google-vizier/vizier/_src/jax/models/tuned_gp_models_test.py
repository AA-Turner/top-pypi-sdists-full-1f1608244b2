# Copyright 2024 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

"""Tests for tuned_gp_models."""

from absl import logging
import equinox as eqx
import jax
import numpy as np
from tensorflow_probability.substrates import jax as tfp
from vizier._src.jax import stochastic_process_model as sp
from vizier._src.jax import types
from vizier._src.jax.models import multitask_tuned_gp_models
from vizier._src.jax.models import tuned_gp_models
from vizier.jax import optimizers

from absl.testing import absltest
from absl.testing import parameterized

tfb = tfp.bijectors
mt_type = multitask_tuned_gp_models.MultiTaskType


class VizierGpTest(parameterized.TestCase):

  def _generate_xys(self, num_metrics: int):
    x_obs = np.array(
        [
            [
                0.2941264,
                0.29313548,
                0.68817519,
                0.37502566,
                0.48356813,
                0.34127283,
            ],
            [
                0.66218224,
                0.70770083,
                0.6901334,
                0.66787973,
                0.5400858,
                0.52721233,
            ],
            [
                0.88469647,
                0.50593371,
                0.83160862,
                0.58674892,
                0.42145673,
                0.31749428,
            ],
            [
                0.39976682,
                0.59517741,
                0.73295106,
                0.6084903,
                0.54891015,
                0.44338632,
            ],
            [
                0.8354305,
                0.87605574,
                0.47855956,
                0.48174861,
                0.37685449,
                0.38348768,
            ],
            [
                0.55608455,
                0.72781129,
                0.52432913,
                0.44291417,
                0.3816395,
                0.326599,
            ],
            [
                0.24689187,
                0.50979672,
                0.67604857,
                0.45172594,
                0.34994392,
                0.75239792,
            ],
            [
                0.71007257,
                0.60896354,
                0.29270877,
                0.74683367,
                0.50169051,
                0.74480515,
            ],
            [
                0.9193235,
                0.24393112,
                0.63868591,
                0.43271524,
                0.43339578,
                0.59413154,
            ],
            [
                0.51850627,
                0.62689204,
                0.76134879,
                0.65990021,
                0.82350868,
                0.7429215,
            ],
        ],
        dtype=np.float64,
    )
    y_obs = np.tile(
        np.array(
            [
                0.55552674,
                -0.29054829,
                -0.04703586,
                0.0217839,
                0.15445438,
                0.46654119,
                0.12255823,
                -0.19540335,
                -0.11772564,
                -0.44447326,
            ],
            dtype=np.float64,
        )[
            :, np.newaxis
        ],  # Added a new axis to be compatible with `np.tile`.
        (1, num_metrics),
    )
    return x_obs, y_obs

  # TODO: Define generic assertions for loss values/masking in
  # coroutines.
  @parameterized.parameters(
      # Pads two observations.
      dict(num_metrics=1, num_obs=12),
      # No observations are padded because multimetric GP does not support
      # observation padding.
      dict(num_metrics=2, num_obs=10),
      dict(
          num_metrics=2,
          num_obs=10,
          multitask_type=mt_type.SEPARABLE_NORMAL_TASK_KERNEL_PRIOR,
      ),
      dict(
          num_metrics=2,
          num_obs=10,
          multitask_type=mt_type.SEPARABLE_LKJ_TASK_KERNEL_PRIOR,
      ),
      dict(
          num_metrics=2,
          num_obs=10,
          multitask_type=mt_type.SEPARABLE_DIAG_TASK_KERNEL_PRIOR,
      ),
  )
  def test_masking_works(
      self,
      num_metrics: int,
      num_obs: int,
      multitask_type: mt_type = mt_type.INDEPENDENT,
  ):
    x_obs, y_obs = self._generate_xys(num_metrics)
    data = types.ModelData(
        features=types.ModelInput(
            # Pads three continuous dimensions.
            continuous=types.PaddedArray.from_array(
                x_obs, target_shape=(num_obs, 9), fill_value=1.0
            ),
            categorical=types.PaddedArray.from_array(
                np.zeros((9, 0), dtype=types.INT_DTYPE),
                target_shape=(num_obs, 2),
                fill_value=1,
            ),
        ),
        labels=types.PaddedArray.from_array(
            y_obs, target_shape=(num_obs, num_metrics), fill_value=np.nan
        ),
    )
    model1 = sp.CoroutineWithData(
        tuned_gp_models.VizierGaussianProcess(
            types.ContinuousAndCategorical[int](9, 2),
            num_metrics,
            _multitask_type=multitask_type,
        ),
        data=data,
    )

    modified_data = types.ModelData(
        features=types.ModelInput(
            continuous=data.features.continuous.replace_fill_value(np.nan),
            categorical=data.features.categorical.replace_fill_value(-1),
        ),
        labels=data.labels,
    )
    model2 = sp.CoroutineWithData(
        tuned_gp_models.VizierGaussianProcess(
            types.ContinuousAndCategorical[int](9, 2),
            num_metrics,
            _multitask_type=multitask_type,
        ),
        data=modified_data,
    )

    # Check that the model loss and optimal parameters are independent of those
    # dimensions and observations.
    optimize = optimizers.JaxoptScipyLbfgsB()
    rng, init_rng = jax.random.split(jax.random.PRNGKey(2), 2)
    optimal_params1, _ = optimize(
        init_params=jax.vmap(model1.setup)(jax.random.split(init_rng, 1)),
        loss_fn=model1.loss_with_aux,
        rng=rng,
        constraints=sp.get_constraints(model1),
    )
    optimal_params2, _ = optimize(
        init_params=jax.vmap(model2.setup)(jax.random.split(init_rng, 1)),
        loss_fn=model2.loss_with_aux,
        rng=rng,
        constraints=sp.get_constraints(model2),
    )

    for key in optimal_params1:
      self.assertTrue(
          np.all(np.equal(optimal_params1[key], optimal_params2[key])),
          msg=f'{key} parameters were not equal.',
      )
    self.assertEqual(
        model1.loss_with_aux(optimal_params1)[0],
        model2.loss_with_aux(optimal_params2)[0],
    )

  @parameterized.parameters(
      # Pads two observations.
      dict(num_metrics=1, num_obs=12),
      # No observations are padded because multimetric GP does not support
      # observation padding.
      dict(num_metrics=2, num_obs=10),
      dict(
          num_metrics=2,
          num_obs=10,
          multitask_type=mt_type.SEPARABLE_NORMAL_TASK_KERNEL_PRIOR,
      ),
      dict(
          num_metrics=2,
          num_obs=10,
          multitask_type=mt_type.SEPARABLE_LKJ_TASK_KERNEL_PRIOR,
      ),
      dict(
          num_metrics=3,
          num_obs=10,
          multitask_type=mt_type.SEPARABLE_DIAG_TASK_KERNEL_PRIOR,
      ),
  )
  def test_good_log_likelihood(
      self,
      num_metrics: int,
      num_obs: int,
      multitask_type: mt_type = mt_type.INDEPENDENT,
  ):
    # We use a fixed random seed for sampling categorical data (and continuous
    # data from `_generate_xys`, above) so that the same data is used for every
    # test run.
    rng, init_rng, cat_rng = jax.random.split(jax.random.PRNGKey(2), 3)
    x_cont_obs, y_obs = self._generate_xys(num_metrics)
    data = types.ModelData(
        features=types.ModelInput(
            continuous=types.PaddedArray.from_array(
                x_cont_obs, target_shape=(num_obs, 9), fill_value=np.nan
            ),
            categorical=types.PaddedArray.from_array(
                jax.random.randint(
                    cat_rng,
                    shape=(num_obs, 3),
                    minval=0,
                    maxval=3,
                    dtype=types.INT_DTYPE,
                ),
                target_shape=(num_obs, 5),
                fill_value=-1,
            ),
        ),
        labels=types.PaddedArray.from_array(
            y_obs, target_shape=(num_obs, num_metrics), fill_value=np.nan
        ),
    )
    target_loss = -0.2
    model = sp.CoroutineWithData(
        tuned_gp_models.VizierGaussianProcess(
            types.ContinuousAndCategorical[int](9, 5),
            num_metrics,
            _multitask_type=multitask_type,
        ),
        data=data,
    )
    optimize = optimizers.JaxoptScipyLbfgsB()
    constraints = sp.get_constraints(model)
    optimal_params, metrics = optimize(
        init_params=jax.vmap(model.setup)(jax.random.split(init_rng, 50)),
        loss_fn=model.loss_with_aux,
        rng=rng,
        constraints=constraints,
    )
    logging.info('Optimal: %s', optimal_params)
    logging.info('Loss: %s', metrics['loss'])
    self.assertLess(np.min(metrics['loss']), target_loss)

  @parameterized.parameters(
      # Pads two observations.
      dict(num_metrics=1, num_obs=12),
      # No observations are padded because multimetric GP does not support
      # observation padding.
      dict(num_metrics=2, num_obs=10),
      dict(
          num_metrics=2,
          num_obs=10,
          multitask_type=mt_type.SEPARABLE_NORMAL_TASK_KERNEL_PRIOR,
      ),
      dict(
          num_metrics=2,
          num_obs=10,
          multitask_type=mt_type.SEPARABLE_LKJ_TASK_KERNEL_PRIOR,
      ),
      dict(
          num_metrics=2,
          num_obs=10,
          multitask_type=mt_type.SEPARABLE_DIAG_TASK_KERNEL_PRIOR,
      ),
  )
  def test_good_log_likelihood_linear(
      self,
      num_metrics: int,
      num_obs: int,
      multitask_type: mt_type = mt_type.INDEPENDENT,
  ):
    """Tests that the GP with linear coef after ARD has good log likelihood.

    The tests use a fixed random seed for sampling categorical data (and
    continuous data from `_generate_xys`, above) so that the same data is used
    for every test run.

    Args:
      num_metrics: Number of metrics.
      num_obs: Number of observations.
      multitask_type: The type of multitask GP to test.
    """
    rng, init_rng, cat_rng = jax.random.split(jax.random.PRNGKey(2), 3)
    x_cont_obs, y_obs = self._generate_xys(num_metrics)
    data = types.ModelData(
        features=types.ModelInput(
            continuous=types.PaddedArray.from_array(
                x_cont_obs, target_shape=(num_obs, 9), fill_value=np.nan
            ),
            categorical=types.PaddedArray.from_array(
                jax.random.randint(
                    cat_rng,
                    shape=(num_obs, 3),
                    minval=0,
                    maxval=3,
                    dtype=types.INT_DTYPE,
                ),
                target_shape=(num_obs, 5),
                fill_value=-1,
            ),
        ),
        labels=types.PaddedArray.from_array(
            y_obs, target_shape=(num_obs, num_metrics), fill_value=np.nan
        ),
    )
    target_loss = -0.2
    model = sp.CoroutineWithData(
        tuned_gp_models.VizierGaussianProcess(
            types.ContinuousAndCategorical[int](9, 5),
            num_metrics,
            _linear_coef=1.0,
            _multitask_type=multitask_type,
        ),
        data=data,
    )
    optimize = optimizers.JaxoptScipyLbfgsB(
        optimizers.LbfgsBOptions(maxiter=100)
    )
    constraints = sp.get_constraints(model)
    best_n = 7
    optimal_params, metrics = optimize(
        init_params=jax.vmap(model.setup)(jax.random.split(init_rng, 50)),
        loss_fn=model.loss_with_aux,
        rng=rng,
        constraints=constraints,
        best_n=best_n,
    )
    logging.info('Optimal: %s', optimal_params)
    logging.info('Loss: %s', metrics['loss'])
    self.assertLess(np.min(metrics['loss']), target_loss)

    best_models = sp.StochasticProcessWithCoroutine(
        coroutine=model.coroutine, params=optimal_params
    )
    predictive = eqx.filter_jit(best_models.precompute_predictive)(data)
    n_pred_features = 6
    cont_pred_feature_dim = 6
    cont_pred_feature_dim_padded = 9
    cat_pred_feature_dim = 3
    cat_pred_feature_dim_padded = 5
    pred_features = types.ModelInput(
        continuous=types.PaddedArray.from_array(
            np.random.normal(size=(n_pred_features, cont_pred_feature_dim)),
            target_shape=(n_pred_features, cont_pred_feature_dim_padded),
            fill_value=np.nan,
        ),
        categorical=types.PaddedArray.from_array(
            np.random.randint(
                3,
                size=(n_pred_features, cat_pred_feature_dim),
                dtype=types.INT_DTYPE,
            ),
            target_shape=(n_pred_features, cat_pred_feature_dim_padded),
            fill_value=-1,
        ),
    )
    y_pred_mean = predictive.predict(pred_features).mean()
    self.assertEqual(
        y_pred_mean.shape,
        (best_n, n_pred_features) + ((num_metrics,) if num_metrics > 1 else ()),
    )


if __name__ == '__main__':
  # Jax disables float64 computations by default and will silently convert
  # float64s to float32s. We must explicitly enable float64.
  jax.config.update('jax_enable_x64', True)
  absltest.main()
