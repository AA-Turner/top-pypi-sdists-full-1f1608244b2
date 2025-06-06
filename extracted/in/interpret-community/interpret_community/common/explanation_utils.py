# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Defines helpful utilities for summarizing and uploading data."""

import logging

import numpy as np
from scipy.sparse import csr_matrix, eye, issparse
from scipy.sparse import vstack as sparse_vstack
from sklearn.preprocessing import normalize
from sklearn.utils import shuffle
from sklearn.utils.sparsefuncs import csc_median_axis_0

from .constants import Scipy
from .gpu_kmeans import kmeans
from .warnings_suppressor import shap_warnings_suppressor

with shap_warnings_suppressor():
    import shap

module_logger = logging.getLogger(__name__)
module_logger.setLevel(logging.INFO)

_VALUES = 'values'
_RANKING = 'ranking'
_FEATURES = 'features'


def reformat_importance_values(local_importance_values, convert_to_list=False):
    """Reformat to match the expected values from different shap versions.

    With shap 0.45.0, the local_importance_values format changed
    from (# classes x # examples x # features)
    to (# examples x # classes x # features).

    :param local_importance_values: The feature importance values.
    :type local_importance_values: numpy.ndarray or scipy.sparse.csr_matrix or list[scipy.sparse.csr_matrix]
    :param convert_to_list: Whether to convert the output to a list.
    :type convert_to_list: bool
    :return: The reformatted feature importance values.
    :rtype: numpy.ndarray or list
    """
    if isinstance(local_importance_values, np.ndarray) and local_importance_values.ndim == 3:
        # Note: this is logic for shap>=0.46.0, which outputs 3d array
        # with shape (# examples x # features x # classes)
        # Move first dimension to last
        local_importance_values = np.moveaxis(local_importance_values, 2, 0)
        if convert_to_list:
            local_importance_values = list(local_importance_values)
    elif not convert_to_list:
        local_importance_values = np.array(local_importance_values)
    return local_importance_values


def _summarize_data(X, k=10, use_gpu=False, to_round_values=True):
    """Summarize a dataset.

    For dense dataset, use k mean samples weighted by the number of data points they
    each represent.
    For sparse dataset, use a sparse row for the background with calculated
    median for dense columns.

    :param X: Matrix of data samples to summarize (# samples x # features).
    :type X: numpy.ndarray or pandas.DataFrame or scipy.sparse.csr_matrix
    :param k: Number of cluster centroids to use for approximation.
    :type k: int
    :param to_round_values: When using kmeans, for each element of every cluster centroid to match the nearest value
        from X in the corresponding dimension. This ensures discrete features
        always get a valid value.  Ignored for sparse data sample.
    :type to_round_values: bool
    :return: summarized numpy array or csr_matrix object.
    :rtype: numpy.ndarray or scipy.sparse.csr_matrix or DenseData
    """
    is_sparse = issparse(X)
    if not str(type(X)).endswith(".DenseData'>"):
        if is_sparse:
            module_logger.debug('Creating sparse data summary as csr matrix')
            # calculate median of sparse background data
            median_dense = csc_median_axis_0(X.tocsc())
            return csr_matrix(median_dense)
        elif len(X) > 10 * k:
            module_logger.debug('Create dense data summary with k-means')
            # use kmeans to summarize the examples for initialization
            # if there are more than 10 x k of them
            if use_gpu:
                return kmeans(X, k, to_round_values)
            else:
                return shap.kmeans(X, k, to_round_values)
    return X


def _should_compress_sparse_matrix(matrix):
    """Returns whether to compress the matrix, which can be sparse or dense format depending on optimal storage.

    If more than a third of the values are non-zero in the sparse matrix, we convert it to dense format.

    :param matrix: The matrix to compress.
    :type matrix: scipy.sparse.csr_matrix or list[scipy.sparse.csr_matrix]
    :return: Whether the matrix should be compressed.
    :rtype: bool
    """
    nnz = 0
    num_cells = 0
    if isinstance(matrix, list):
        for class_matrix in matrix:
            nnz += class_matrix.nnz
            num_cells += class_matrix.shape[0] * class_matrix.shape[1]
    else:
        nnz += matrix.nnz
        num_cells += matrix.shape[0] * matrix.shape[1]
    return nnz > num_cells / 3


def _get_raw_feature_importances(importance_values, raw_to_output_feature_maps):
    """Return raw feature importance values.

    :param importance_values: The importance values computed for the dataset.
    :type importance_values: numpy.ndarray or list[scipy.sparse.csr_matrix]
    :param raw_to_output_feature_maps: A list of feature maps from raw to generated feature.
    :type raw_to_output_feature_maps: list[Union[numpy.ndarray, scipy.sparse.csr_matrix]]
    :return: Raw feature importance values.
    :rtype: numpy.ndarray
    """
    if not isinstance(raw_to_output_feature_maps, list):
        raise ValueError("raw_to_output_feature_maps should be a list of feature maps")
    if any(map(lambda x: (x < 0).sum(), raw_to_output_feature_maps)):
        raise ValueError("Feature maps should only contain non-negative values")
    if any(map(lambda x: not _is_one_to_many(x), raw_to_output_feature_maps)):
        print("Many to one/many maps found in input")

    raw_to_output_map = raw_to_output_feature_maps[0]
    for fmap in raw_to_output_feature_maps[1:]:
        if _is_identity(fmap):
            continue
        raw_to_output_map = raw_to_output_map.dot(fmap)

    # normalize column wise
    raw_to_output_map = normalize(raw_to_output_map, norm='l1', axis=0)

    orig_single_dimensional_importances = False
    if isinstance(importance_values, list):
        raw_importances = []
        for class_matrix in importance_values:
            raw_matrix = class_matrix.dot(raw_to_output_map.T)
            raw_importances.append(raw_matrix)
        is_sparse_matrix = len(raw_importances) > 0 and issparse(raw_importances[0])
        if is_sparse_matrix:
            if _should_compress_sparse_matrix(raw_importances):
                for i in range(len(raw_importances)):
                    raw_importances[i] = raw_importances[i].toarray()
                raw_importances = np.array(raw_importances)
        else:
            raw_importances = np.array(raw_importances)
        return raw_importances

    if len(importance_values.shape) < 2:
        importance_values = importance_values.reshape(1, -1)
        orig_single_dimensional_importances = True

    if issparse(raw_to_output_map):
        if len(importance_values.shape) > 2:
            raw_importances = _multiply_sparse_matrix_3d_numpy_tensor(importance_values, raw_to_output_map.T)
        else:
            if _is_identity(raw_to_output_map):
                raw_importances = importance_values
            else:
                raw_importances = raw_to_output_map.dot(importance_values.T).T
            if issparse(raw_importances) and _should_compress_sparse_matrix(raw_importances):
                raw_importances = raw_importances.toarray()
    else:
        raw_importances = importance_values.dot(raw_to_output_map.T)
    return raw_importances.squeeze(0) if orig_single_dimensional_importances else raw_importances


def _is_identity(matrix):
    """Checks if the given sparse matrix is identity matrix.

    :param matrix: sparse matrix
    :type matrix: scipy.sparse.csr_matrix
    :return: True if the matrix is an identity matrix.
    :rtype: bool
    """
    if not issparse(matrix):
        return False
    sh0 = matrix.shape[0]
    sh1 = matrix.shape[1]
    return sh0 == sh1 and matrix.nnz == sh0 and (matrix - eye(sh0, format=Scipy.CSR_FORMAT)).nnz == 0


def _multiply_sparse_matrix_3d_numpy_tensor(np_tensor, sp_matrix):
    """Multiply sparse matrix with a 3 dimension numpy array.

    :param np_tensor: numpy tensor of 3 dimensions.
    :type np_tensor: numpy.ndarray
    :param sp_matrix: sparse matrix
    :type sp_matrix: scipy.sparse.csr_matrix
    :return: The product of numpy array and sparse matrix.
    :rtype: numpy.ndarray
    """
    if len(np_tensor.shape) != 3:
        raise ValueError("Expected matrix of dimension 3. Got dimension {}.".format(len(np_tensor.shape)))

    output = np.zeros((*np_tensor.shape[:-1], sp_matrix.shape[1]))
    for i in range(np_tensor.shape[0]):
        output[i] = sp_matrix.T.dot(np_tensor[i].T).T

    return output


def _is_one_to_many(feature_map):
    return ((feature_map > 0).sum(axis=0) >= 2).sum() == 0


def _get_dense_examples(examples):
    if issparse(examples):
        module_logger.debug('converting sparse examples to regular array')
        return examples.toarray()
    return examples


def _convert_to_list(shap_values):
    module_logger.debug('converting numpy array of list of numpy array to list')
    classification = isinstance(shap_values, list)
    if classification:
        # shap_values is a list of ndarrays
        shap_values_numpy_free = []
        for array in shap_values:
            shap_values_numpy_free.append(array.tolist())
        return shap_values_numpy_free
    else:
        # shap_values is a single ndarray
        return shap_values.tolist()


def _generate_augmented_data(x, max_num_of_augmentations=np.inf):
    """Augment x by appending x with itself shuffled columnwise many times.

    :param x: data that has to be augmented, array or sparse matrix of 2 dimensions
    :type x: numpy.ndarray or scipy.sparse.csr_matrix
    :param max_augment_data_size: number of times we stack permuted x to augment.
    :type max_augment_data_size: int
    :return: augmented data with roughly number of rows that are equal to number of columns
    :rtype: numpy.ndarray or scipy.sparse.csr_matrix
    """
    x_augmented = x
    vstack = sparse_vstack if issparse(x) else np.vstack
    for i in range(min(x.shape[1] // x.shape[0] - 1, max_num_of_augmentations)):
        x_permuted = shuffle(x.T, random_state=i).T
        x_augmented = vstack([x_augmented, x_permuted])

    return x_augmented


def _scale_tree_shap(shap_values, expected_values, prediction):
    """Scale the log odds shap values from TreeExplainer to be in terms of probability.

    Note this is just an approximation, since the logistic function is non-linear.
    The function is a modified version of the implementations posted on shap github issues:
    https://github.com/slundberg/shap/issues/29#issuecomment-374928027
    https://github.com/slundberg/shap/issues/29#issuecomment-408385378

    :param shap_values: The shap values to transform from log odds to probabilities.
    :type shap_values: numpy.ndarray
    :param expected_values: The expected values as probabilities.
    :type expected_values: numpy.ndarray
    :param prediction: The predicted probability from the teacher model.
    :type prediction: numpy.ndarray
    :return: The transformed tree shap values as probabilities.
    :rtype: list or numpy.ndarray
    """
    # In multiclass case, use expected values and predictions per class
    if isinstance(shap_values, list):
        values_to_convert = shap_values
        for idx, shap_values in enumerate(values_to_convert):
            values_to_convert[idx] = _scale_single_shap_matrix(shap_values, expected_values[idx], prediction[:, idx])
        return values_to_convert
    else:
        if len(prediction.shape) == 1:
            return _scale_single_shap_matrix(shap_values, expected_values, prediction)
        else:
            # Note: in binary classification with teacher probability this will be index 1,
            # but in binary classification with surrogate probability this will be index 0
            return _scale_single_shap_matrix(shap_values, expected_values, prediction[:, -1])


def _scale_single_shap_matrix(shap_values, expectation, prediction):
    """Scale a single class matrix of shap values to sum to the teacher model prediction.

    :param shap_values: The shap values of the mimic model.
    :type shap_values: numpy.ndarray
    :param expected_values: The expected values as probabilities (base values).
    :type expected_values: numpy.ndarray
    :param prediction: The predicted probability from the teacher model.
    :type prediction: numpy.ndarray
    :return: The transformed tree shap values as probabilities.
    :rtype: list or numpy.ndarray
    """
    mimic_prediction = np.sum(shap_values, axis=1)
    error = prediction - mimic_prediction - expectation
    absolute_error = np.abs(error)
    if not isinstance(absolute_error, np.ndarray):
        absolute_error = np.array(absolute_error)
    error_sign = np.sign(error)
    if not isinstance(error_sign, np.ndarray):
        error_sign = np.array(error_sign)
    absolute_shap_vector = np.abs(shap_values)
    absolute_shap_magnitude = np.sum(absolute_shap_vector, axis=1)
    # We divide by one, when we know the numerator is 0
    safe_absolute_magnitude_denominator = np.where(absolute_shap_magnitude > 0., absolute_shap_magnitude, 1)
    flat_magnitude = np.multiply(np.maximum(absolute_error - absolute_shap_magnitude, 0.), error_sign)
    feature_dimension = shap_values.shape[1]
    proportional_correction = np.divide(
        np.multiply(
            np.multiply(
                error_sign,
                np.minimum(absolute_error, absolute_shap_magnitude))[:, None],
            absolute_shap_vector),
        safe_absolute_magnitude_denominator[:, None])
    flat_correction = np.full(shap_values.shape, np.divide(flat_magnitude[:, None], feature_dimension))
    return shap_values + proportional_correction + flat_correction


def _convert_single_instance_to_multi(instance_shap_values):
    """Convert a single shap values instance to multi-instance form.

    :param instance_shap_values: The shap values calculated for a new instance.
    :type instance_shap_values: numpy.ndarray or list
    :return: The instance converted to multi-instance form.
    :rtype: numpy.ndarray or list
    """
    classification = isinstance(instance_shap_values, list)
    if classification:
        shap_values = instance_shap_values
        for i in range(len(shap_values)):
            shap_values[i] = shap_values[i].reshape(1, -1)
    else:
        shap_values = instance_shap_values
    return shap_values


def _append_shap_values_instance(shap_values, instance_shap_values):
    """Append a single instance of shap values to an existing multi-instance shap values list or array.

    :param shap_values: The existing shap values array or list.
    :type shap_values: numpy.ndarray or list
    :param instance_shap_values: The shap values calculated for a new instance.
    :type instance_shap_values: numpy.ndarray or list
    :return: The instance appended to the existing shap values.
    :rtype: numpy.ndarray or list
    """
    classification = isinstance(instance_shap_values, list)
    if classification:
        for i in range(len(shap_values)):
            cols_dim = len(instance_shap_values[i].shape)
            # col_dim can only be 1 or 2 here, depending on data passed to shap
            if cols_dim != 2:
                output_size = shap_values[i].shape[-1]
                tmp_shap_values_2d = instance_shap_values[i].reshape(1, output_size)
            else:
                tmp_shap_values_2d = instance_shap_values[i]
            # Append rows
            shap_values[i] = np.append(shap_values[i], tmp_shap_values_2d, axis=0)
    else:
        shap_values = np.append(shap_values, instance_shap_values, axis=0)
    return shap_values


def _fix_linear_explainer_shap_values(model, shap_values):
    """Update the shap values from LinearExplainer in case the shape does not conform to API standards.

    :param model: The linear model.
    :type model: tuple of (coefficients, intercept) or sklearn.linear.* model
    :param shap_values: The existing shap values array or list.
    :type shap_values: numpy.ndarray or list
    :return: The shap values reshaped into the correct form for given linear model.
    :rtype: numpy.ndarray or list
    """
    # Temporary fix for a bug in shap for regression models
    if (isinstance(model, tuple) and len(model) == 2):
        coef = model[0]
    elif hasattr(model, 'coef_') and hasattr(model, 'intercept_'):
        coef = model.coef_
    else:
        raise Exception('An unknown model type was passed: ' + str(type(model)))
    coef_shape_len = len(np.array(coef).shape)
    shap_values_shape_len = len(np.array(shap_values).shape)
    if coef_shape_len == 1 and shap_values_shape_len == 3:
        shap_values = shap_values[0]
    elif coef_shape_len == 2 and shap_values_shape_len == 2:
        shap_values = [-shap_values, shap_values]
    return shap_values


def _sort_values(values, order):
    return np.array(values)[order]


def _unsort_1d(values, order):
    """Unsort a sorted 1d array based on the order that was used to sort it.

    :param values: The array that has been sorted.
    :type values: numpy.ndarray
    :param order: The order list that was originally used to sort values.
    :type order: numpy.ndarray
    :return: The unsorted array.
    :rtype: numpy.ndarray
    """
    order_inverse = [None] * len(order)
    for i in range(len(order)):
        order_inverse[order[i]] = i
    return np.array(values)[order_inverse]


def _order_imp(summary):
    """Compute the ranking of feature importance values.

    :param summary: A 3D array of the feature importance values to be ranked.
    :type summary: numpy.ndarray
    :return: The rank of the feature importance values.
    :rtype: numpy.ndarray
    """
    return summary.argsort()[..., ::-1]


def _sparse_order_imp_csr_matrix(local_importance_values, values_type=_RANKING, features=None, top_k=None):
    """Compute the ranking, names or values for sparse feature importance values on a single csr_matrix.

    :param local_importance_values: The local importance values to compute the ranking for.
    :type local_importance_values: scipy.sparse.csr_matrix
    :param values_type: The type of values, can be 'ranking', which returns the sorted
        indices, 'values', which returns the sorted values, or 'features', which returns
        the feature names.
    :type values_type: str
    :param features: The feature names.
    :type features: list[str]
    :param top_k: If specified, only the top k values will be returned.
    :type top_k: int
    :return: The rank of the non-zero sparse feature importance values.
    :rtype: list
    """
    sparse_ranking = []
    data = local_importance_values.data
    indices = local_importance_values.indices
    indptr = local_importance_values.indptr
    for i in range(len(indptr) - 1):
        rowstart = indptr[i]
        rowend = indptr[i + 1]
        row_values = data[rowstart:rowend]
        # compute the ranking of the values for each row
        values_ranking = row_values.argsort()[..., ::-1]
        if values_type == _VALUES:
            sorted_values = row_values[values_ranking]
            if top_k is not None:
                sorted_values = sorted_values[:top_k]
            sparse_ranking.append(sorted_values.tolist())
        elif values_type == _FEATURES:
            row_indices = indices[rowstart:rowend]
            indices_ranking = row_indices[values_ranking]
            if features is not None:
                ranked_features = np.array(features)[indices_ranking]
                if top_k is not None:
                    ranked_features = ranked_features[:top_k]
                sparse_ranking.append(ranked_features.tolist())
            else:
                if top_k is not None:
                    indices_ranking = indices_ranking[:top_k]
                sparse_ranking.append(indices_ranking.tolist())
        elif values_type == _RANKING:
            row_indices = indices[rowstart:rowend]
            # re-shuffle indices based on the ranking values
            indices_ranking = row_indices[values_ranking]
            if top_k is not None:
                indices_ranking = indices_ranking[:top_k]
            sparse_ranking.append(indices_ranking.tolist())
        else:
            raise ValueError("Unknown values_type specified: {}.".format(values_type))
    return sparse_ranking


def _sparse_order_imp(local_importance_values, values_type=_RANKING, features=None, top_k=None):
    """Compute the ranking for sparse feature importance values.

    :param local_importance_values: The local importance values to compute the ranking for.
    :type local_importance_values: scipy.sparse.csr_matrix or list[scipy.sparse.csr_matrix]
    :param values_type: The type of values, can be 'ranking', which returns the sorted
        indices, 'values', which returns the sorted values, or 'features', which returns
        the feature names.
    :type values_type: str
    :param features: The feature names.
    :type features: list[str]
    :param top_k: If specified, only the top k values will be returned.
    :type top_k: int
    :return: The rank of the non-zero sparse feature importance values.
    :rtype: list
    """
    if isinstance(local_importance_values, list):
        per_class_sparse_ranking = []
        for class_importance_values in local_importance_values:
            per_class_sparse_ranking.append(_sparse_order_imp_csr_matrix(class_importance_values,
                                                                         values_type=values_type,
                                                                         features=features,
                                                                         top_k=top_k))
        return per_class_sparse_ranking
    else:
        return _sparse_order_imp_csr_matrix(local_importance_values,
                                            values_type=values_type,
                                            features=features,
                                            top_k=top_k)


# sorts a single dimensional feature list according to order
def _sort_feature_list_single(features, order):
    return list(map(lambda x: features[x], order))


# returns a list of lists, where each internal list is the feature list sorted according to the order of a single class
def _sort_feature_list_multiclass(features, order):
    if hasattr(features, 'tolist'):
        features = features.tolist()
    return [list(map(lambda x: features[x], order_i)) for order_i in order]


# do the equivalent of a numpy array slice on a two-dimensional list
def _two_dimensional_slice(lst, end_index):
    return list(map(lambda x: x[:end_index], lst))


def _get_feature_map_from_list_of_indexes(indices_list):
    """Compute feature map from a list of indices from raw features to generated feature indices.

    :param indices_list: A list of lists of generated feature indices for each raw feature.
    :type indices_list: list[list[int]]
    :return: A feature map from raw to generated.
    :rtype: numpy.ndarray
    """
    # sets for each list of generated features
    raw_to_gen = []
    for generated_index_list in indices_list:
        raw_to_gen.append(set(generated_index_list))

    num_gen_feats = 1 + max([max(x) for x in indices_list])
    num_raw = len(indices_list)
    # compute number of parents for a generated feature
    weights = np.zeros((num_gen_feats))
    for i in range(num_gen_feats):
        gen_feat_num_parents = sum([1 for gen_set in raw_to_gen if i in gen_set])
        if gen_feat_num_parents:
            # divide a generated feature weight equally amongst the raw features.
            weights[i] = 1.0 / gen_feat_num_parents

    feature_map = np.zeros((num_raw, num_gen_feats))
    for i in range(len(indices_list)):
        for j in indices_list[i]:
            feature_map[i, j] = weights[j]

    return feature_map
