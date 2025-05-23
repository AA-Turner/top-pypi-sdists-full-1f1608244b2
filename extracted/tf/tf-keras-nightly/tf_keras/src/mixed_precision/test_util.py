# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
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
# ==============================================================================
"""Contains testing utilities related to mixed precision."""

import tensorflow.compat.v2 as tf

from tf_keras.src import regularizers
from tf_keras.src.engine import base_layer


def create_identity_with_grad_check_fn(expected_gradient, expected_dtype=None):
    """Returns a function that asserts it's gradient has a certain value.

    This serves as a hook to assert intermediate gradients have a certain value.
    This returns an identity function. The identity's gradient function is also
    the identity function, except it asserts that the gradient equals
    `expected_gradient` and has dtype `expected_dtype`.

    Args:
      expected_gradient: The gradient function asserts that the gradient is this
        value.
      expected_dtype: The gradient function asserts the gradient has this dtype.

    Returns:
      An identity function whose gradient function asserts the gradient has a
      certain value.
    """

    @tf.custom_gradient
    def _identity_with_grad_check(x):
        """Function that asserts it's gradient has a certain value."""
        x = tf.identity(x)

        def grad(dx):
            """Gradient function that asserts the gradient has a certain
            value."""
            if expected_dtype:
                assert (
                    dx.dtype == expected_dtype
                ), f"dx.dtype should be {expected_dtype} but is: {dx.dtype}"
            expected_tensor = tf.convert_to_tensor(
                expected_gradient, dtype=dx.dtype, name="expected_gradient"
            )
            # Control dependency is to ensure input is available. It's possible
            # the dataset will throw a StopIteration to indicate there is no
            # more data, in which case we don't want to run the assertion.
            with tf.control_dependencies([x]):
                assert_op = tf.compat.v1.assert_equal(dx, expected_tensor)
            with tf.control_dependencies([assert_op]):
                dx = tf.identity(dx)
            return dx

        return x, grad

    # TF-Keras sometimes has trouble serializing Lambda layers with a decorated
    # function. So we define and return a non-decorated function.
    def identity_with_grad_check(x):
        return _identity_with_grad_check(x)

    return identity_with_grad_check


def create_identity_with_nan_gradients_fn(have_nan_gradients):
    """Returns a function that optionally has NaN gradients.

    This serves as a hook to introduce NaN gradients to a model. This returns an
    identity function. The identity's gradient function will check if the
    boolean tensor `have_nan_gradients` is True. If so, the gradient will be
    NaN.  Otherwise, the gradient will also be the identity.

    Args:
      have_nan_gradients: A scalar boolean tensor. If True, gradients will be
        NaN. Otherwise, the gradient function is the identity function.

    Returns:
      An identity function whose gradient function will return NaNs, if
      `have_nan_gradients` is True.
    """

    @tf.custom_gradient
    def _identity_with_nan_gradients(x):
        """Function whose gradient is NaN iff `have_nan_gradients` is True."""
        x = tf.identity(x)

        def grad(dx):
            return tf.cond(
                have_nan_gradients, lambda: dx * float("NaN"), lambda: dx
            )

        return x, grad

    # TF-Keras sometimes has trouble serializing Lambda layers with a decorated
    # function. So we define and return a non-decorated function.
    def identity_with_nan_gradients(x):
        return _identity_with_nan_gradients(x)

    return identity_with_nan_gradients


class AssertTypeLayer(base_layer.Layer):
    """A layer which asserts it's inputs are a certain type."""

    def __init__(self, assert_type=None, **kwargs):
        self._assert_type = (
            tf.as_dtype(assert_type).name if assert_type else None
        )
        super().__init__(**kwargs)

    def assert_input_types(self, inputs):
        """Asserts `inputs` are of the correct type. Should be called in
        call()."""
        if self._assert_type:
            inputs_flattened = tf.nest.flatten(inputs)
            for inp in inputs_flattened:
                assert inp.dtype.base_dtype == self._assert_type, (
                    "Input tensor has type %s which does "
                    "not match assert type %s"
                    % (inp.dtype.name, self._assert_type)
                )


class MultiplyLayer(AssertTypeLayer):
    """A layer which multiplies its input by a scalar variable."""

    def __init__(
        self,
        regularizer=None,
        activity_regularizer=None,
        use_operator=False,
        var_name="v",
        **kwargs,
    ):
        """Initializes the MultiplyLayer.

        Args:
          regularizer: The weight regularizer on the scalar variable.
          activity_regularizer: The activity regularizer.
          use_operator: If True, add using the * operator. If False, add using
            tf.multiply.
          var_name: The name of the variable. It can be useful to pass a name
            other than 'v', to test having the attribute name (self.v) being
            different from the variable name.
          **kwargs: Passed to AssertTypeLayer constructor.
        """
        self._regularizer = regularizer
        if isinstance(regularizer, dict):
            self._regularizer = regularizers.deserialize(
                regularizer, custom_objects=globals()
            )
        self._activity_regularizer = activity_regularizer
        if isinstance(activity_regularizer, dict):
            self._activity_regularizer = regularizers.deserialize(
                activity_regularizer, custom_objects=globals()
            )

        self._use_operator = use_operator
        self._var_name = var_name
        super().__init__(
            activity_regularizer=self._activity_regularizer, **kwargs
        )

    def build(self, input_shape):
        self.v = self.add_weight(
            self._var_name,
            (),
            initializer="ones",
            regularizer=self._regularizer,
        )
        super().build(input_shape)

    def call(self, inputs):
        self.assert_input_types(inputs)
        return self._multiply(inputs, self.v)

    def _multiply(self, x, y):
        if self._use_operator:
            return x * y
        else:
            return tf.multiply(x, y)

    def get_config(self):
        config = super().get_config()
        config["regularizer"] = regularizers.serialize(self._regularizer)
        config["activity_regularizer"] = regularizers.serialize(
            self._activity_regularizer
        )
        config["use_operator"] = self._use_operator
        config["var_name"] = self._var_name
        config["assert_type"] = self._assert_type
        return config


class MultiplyLayerWithoutAutoCast(MultiplyLayer):
    """Same as MultiplyLayer, but does not use AutoCastVariables."""

    def build(self, input_shape):
        dtype = self.dtype
        if dtype in ("float16", "bfloat16"):
            dtype = "float32"
        self.v = self.add_weight(
            "v",
            (),
            initializer="ones",
            dtype=dtype,
            autocast=False,
            regularizer=self._regularizer,
        )
        # Call Layer.build() to skip MultiplyLayer.build() which we override.
        base_layer.Layer.build(self, input_shape)

    def call(self, inputs):
        self.assert_input_types(inputs)
        assert self.v.dtype in (tf.float32, tf.float64)
        return self._multiply(inputs, tf.cast(self.v, inputs.dtype))


class IdentityRegularizer(regularizers.Regularizer):
    def __call__(self, x):
        assert x.dtype == tf.float32
        return tf.identity(x)

    def get_config(self):
        return {}


class ReduceSumRegularizer(regularizers.Regularizer):
    def __call__(self, x):
        return tf.reduce_sum(x)

    def get_config(self):
        return {}

