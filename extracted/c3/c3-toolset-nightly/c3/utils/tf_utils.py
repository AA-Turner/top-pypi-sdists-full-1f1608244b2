"""Various utility functions to speed up tensorflow coding."""

import numpy as np
import tensorflow as tf
from tensorflow.python.client import device_lib
import os
from c3.utils.qt_utils import pauli_basis, projector
from typing import Callable, List
import tensorflow_probability as tfp


def tf_setup():
    gpus = tf.config.experimental.list_physical_devices("GPU")
    if gpus:
        try:
            # Currently, memory growth needs to be the same across GPUs
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            logical_gpus = tf.config.experimental.list_logical_devices("GPU")
            print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
        except RuntimeError as e:
            # Memory growth must be set before GPUs have been initialized
            print(e)


def tf_log_level_info():
    """Display the information about different log levels in tensorflow."""
    info = (
        "Log levels of tensorflow:\n"
        "\t0 = all messages are logged (default behavior)\n"
        "\t1 = INFO messages are not printed\n"
        "\t2 = INFO and WARNING messages are not printed\n"
        "\t3 = INFO, WARNING, and ERROR messages are not printed\n"
    )
    print(info)


def get_tf_log_level():
    """Display the current tensorflow log level of the system."""
    log_lvl = "0"

    if "TF_CPP_MIN_LOG_LEVEL" in os.environ:
        log_lvl = os.environ["TF_CPP_MIN_LOG_LEVEL"]

    return log_lvl


def set_tf_log_level(lvl):
    """
    Set tensorflows system log level.

    REMARK: it seems like the 'TF_CPP_MIN_LOG_LEVEL' variable expects a string.
            the input of this function seems to work with both string and/or
            integer, as casting string to string does nothing. feels hacked?
            but I guess it's just python...
    """
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = str(lvl)


def tf_list_avail_devices():
    """
    List available devices.

    Function for displaying all available devices for tf_setuptensorflow
    operations on the local machine.

    TODO:   Refine output of this function. But without further knowledge
            about what information is needed, best practise is to output all
            information available.
    """
    local_dev = device_lib.list_local_devices()
    print(local_dev)


def tf_limit_gpu_memory(memory_limit):
    """
    Set a limit for the GPU memory.

    """
    gpus = tf.config.experimental.list_physical_devices("GPU")
    if gpus:
        # Restrict TensorFlow to only allocate 1GB of memory on the first GPU
        try:
            tf.config.experimental.set_virtual_device_configuration(
                gpus[0],
                [
                    tf.config.experimental.VirtualDeviceConfiguration(
                        memory_limit=memory_limit
                    )
                ],
            )
            logical_gpus = tf.config.experimental.list_logical_devices("GPU")
            print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
        except RuntimeError as e:
            # Virtual devices must be set before GPUs have been initialized
            print(e)


def tf_measure_operator(M, rho):
    """
    Expectation value of a quantum operator by tracing with a density matrix.

    Parameters
    ----------
    M : tf.tensor
        A quantum operator.
    rho : tf.tensor
        A density matrix.

    Returns
    -------
    tf.tensor
        Expectation value.

    """
    return tf.linalg.trace(tf.matmul(M, rho))


# MATRIX MULTIPLICATION FUNCTIONS
def tf_matmul_left(dUs: tf.Tensor):
    """
    Parameters:
        dUs: tf.Tensor
            Tensorlist of shape (N, n,m)
            with number N matrices of size nxm
    Multiplies a list of matrices from the left.

    """
    return tf.foldr(lambda a, x: tf.matmul(a, x), dUs)


def tf_matmul_right(dUs):
    """
    Parameters:
        dUs: tf.Tensor
            Tensorlist of shape (N, n,m)
            with number N matrices of size nxm
    Multiplies a list of matrices from the right.

    """
    return tf.foldl(lambda a, x: tf.matmul(a, x), dUs)


def tf_matmul_n(tensor_list: tf.Tensor, folding_stack: List[Callable]) -> tf.Tensor:
    """Multipy a list of tensors using a precompiled stack of function to apply to each layer of a binary tree.

    Parameters
    ----------
    tensor_list : List[tf.Tensor]
        Matrices to be multiplied.
    folding_stack : List[Callable]
        List of functions to multiply each layer.

    Returns
    -------
    tf.Tensor
        Reduced product of matrices.
    """
    for func in folding_stack:
        even = tensor_list[0::2]
        odd = tensor_list[1::2]
        tensor_list = func(odd, even)
    return tensor_list[0]


def _tf_matmul_n_even(odd: tf.Tensor, even: tf.Tensor) -> tf.Tensor:
    """Batch matmul for tensors with equal batch dimesion.

    Parameters
    ----------
    odd : tf.Tensor
    even : tf.Tensor

    Returns
    -------
    tf.Tensor
    """
    return tf.matmul(odd, even)


def _tf_matmul_n_odd(odd: tf.Tensor, even: tf.Tensor) -> tf.Tensor:
    """Batch matmul for tensors where the batch dimension of even is 1 longer than odd.

    Parameters
    ----------
    odd : tf.Tensor
    even : tf.Tensor

    Returns
    -------
    tf.Tensor
    """
    return tf.concat([tf.matmul(odd, even[:-1]), tf.expand_dims(even[-1], 0)], 0)


# MATH FUNCTIONS
def tf_log10(x):
    """Tensorflow had no logarithm with base 10. This is ours."""
    numerator = tf.log(x)
    denominator = tf.log(tf.constant(10, dtype=numerator.dtype))
    return numerator / denominator


def tf_abs_squared(x):
    """Rewritten so that is has a gradient."""
    return tf.reshape(tf.cast(tf.math.conj(x) * x, dtype=tf.float64), shape=[1])


def tf_complexify(x):
    return tf.complex(x, tf.zeros_like(x))


def tf_abs(x):
    """Rewritten so that is has a gradient."""
    # TODO: See if custom abs and abs_squared are needed and compare performance.
    return tf.sqrt(tf_abs_squared(x))


def tf_ave(x: list):
    """Take average of a list of values in tensorflow."""
    return tf.add_n(x) / len(x)


def tf_diff(l):  # noqa
    """
    Running difference of the input list l. Equivalent to np.diff, except it
    returns the same shape by adding a 0 in the last entry.
    """
    dim = tf.shape(l)[0] - 1
    diagonal = tf.constant([-1] * dim + [0], dtype=l.dtype)
    offdiagonal = tf.constant([1] * dim, dtype=l.dtype)
    proj = tf.linalg.diag(diagonal) + tf.linalg.diag(offdiagonal, k=1)
    return tf.linalg.matvec(proj, l)


# MATRIX FUNCTIONS

# TODO - change A.shape[: length-2] to tf.shape
def Id_like(A):
    """Identity of the same size as A."""
    length = len(tf.shape(A))  # TF does not like negative pythonic indexing
    return tf.eye(
        tf.shape(A)[length - 1], batch_shape=A.shape[: length - 2], dtype=A.dtype
    )


#
# def tf_kron(A, B):
#     """Kronecker product of 2 matrices."""
#     dims = tf.shape(A) * tf.shape(B)
#     tensordot = tf.tensordot(A, B, axes=0)
#     reshaped = tf.reshape(tf.transpose(tensordot, perm=[0, 2, 1, 3]), dims)
#     return reshaped


def tf_kron(A, B):
    """Kronecker product of 2 matrices. Can be applied with batch dimmensions."""
    dims = tf.convert_to_tensor(
        [tf.shape(A)[-2] * tf.shape(B)[-2], tf.shape(A)[-1] * tf.shape(B)[-1]]
    )
    res = tf.expand_dims(tf.expand_dims(A, -1), -3) * tf.expand_dims(
        tf.expand_dims(B, -2), -4
    )
    if tf.size(tf.shape(res)) > 4:
        dims = tf.concat([[tf.shape(res)[0]], dims], 0)
    return tf.reshape(res, dims)


# SUPEROPER FUNCTIONS
def tf_spre(A):
    """Superoperator on the left of matrix A."""
    Id = Id_like(A)
    return tf_kron(A, Id)


def tf_spost(A):
    """Superoperator on the right of matrix A."""
    Id = Id_like(A)
    return tf_kron(Id, tf.linalg.matrix_transpose(A))


#
def tf_super(A):
    """Superoperator from both sides of matrix A."""
    superA = tf.matmul(
        tf_spre(A), tf_spost(tf.linalg.matrix_transpose(A, conjugate=True))
    )
    return superA


def tf_state_to_dm(psi_ket):
    """Make a state vector into a density matrix."""
    psi_ket = tf.reshape(psi_ket, [tf.shape(psi_ket)[0], 1])
    psi_bra = tf.transpose(psi_ket)
    return tf.matmul(psi_ket, psi_bra)


# TODO see which code to get dv is better (and kill the other)
def tf_dm_to_vec(dm):
    """Convert a density matrix into a density vector."""
    return tf.reshape(tf.transpose(dm), shape=[-1, 1])


def tf_vec_to_dm(vec):
    """Convert a density vector to a density matrix."""
    dim = tf.sqrt(tf.cast(tf.shape(vec)[0], tf.float32))
    return tf.transpose(tf.reshape(vec, [dim, dim]))


def tf_dmdm_fid(rho, sigma):
    """Trace fidelity between two density matrices."""
    # TODO needs fixing
    rhosqrt = tf.linalg.sqrtm(rho)
    return tf.linalg.trace(
        tf.linalg.sqrtm(tf.matmul(tf.matmul(rhosqrt, sigma), rhosqrt))
    )


def tf_dmket_fid(rho, psi):
    """Fidelity between a state vector and a density matrix."""
    return tf.sqrt(tf.matmul(tf.matmul(tf.linalg.adjoint(psi), rho), psi))


def tf_ketket_fid(psi1, psi2):
    """Overlap of two state vectors."""
    return tf_abs(tf.matmul(tf.linalg.adjoint(psi1), psi2))


def tf_unitary_overlap(A: tf.Tensor, B: tf.Tensor, lvls: tf.Tensor = None) -> tf.Tensor:
    """Unitary overlap between two matrices.

    Parameters
    ----------
    A : tf.Tensor
        Unitary A
    B : tf.Tensor
        Unitary B
    lvls : tf.Tensor, optional
        Levels, by default None

    Returns
    -------
    tf.Tensor
        Overlap between the two unitaries

    Raises
    ------
    TypeError
        For errors during cast
    ValueError
        For errors during matrix multiplicaton
    """
    try:
        if lvls is None:
            lvls = tf.cast(tf.shape(B)[0], B.dtype)
        overlap = tf_abs_squared(
            tf.linalg.trace(tf.matmul(A, tf.linalg.adjoint(B))) / lvls
        )
    except TypeError:
        raise TypeError("Possible Inconsistent Dimensions while casting tensors")
    except ValueError:
        raise ValueError(
            "Possible Inconsistent Dimensions during Matrix Multiplication"
        )
    return overlap


def tf_superoper_unitary_overlap(A, B, lvls=None):
    # TODO: This is just wrong, probably.
    if lvls is None:
        lvls = tf.sqrt(tf.cast(tf.shape(B)[0], B.dtype))
    overlap = (
        tf_abs(tf.sqrt(tf.linalg.trace(tf.matmul(A, tf.linalg.adjoint(B)))) / lvls) ** 2
    )

    return overlap


def tf_average_fidelity(A, B, lvls=None):
    """A very useful but badly named fidelity measure."""
    if lvls is None:
        lvls = [tf.cast(tf.shape(B)[0], B.dtype)]
    Lambda = tf.matmul(tf.linalg.adjoint(A), B)
    return tf_super_to_fid(tf_super(Lambda), lvls)


def tf_superoper_average_fidelity(A, B, lvls=None):
    """A very useful but badly named fidelity measure."""
    if lvls is None:
        lvls = tf.sqrt(tf.cast(tf.shape(B)[0], B.dtype))
    lambda_super = tf.matmul(tf.linalg.adjoint(tf_project_to_comp(A, lvls, True)), B)
    return tf_super_to_fid(lambda_super, lvls)


def tf_super_to_fid(err, lvls):
    """Return average fidelity of a process."""
    lambda_chi = tf_choi_to_chi(super_to_choi(err), dims=lvls)
    d = 2 ** len(lvls)
    # get only 00 element and measure fidelity
    return tf_abs((lambda_chi[0, 0] / d + 1) / (d + 1))


def tf_choi_to_chi(U, dims=None):
    """
    Convert the choi representation of a process to chi representation.

    """
    if dims is None:
        dims = [tf.sqrt(tf.cast(tf.shape(U)[0], U.dtype))]
    B = tf.constant(pauli_basis([2] * len(dims)), dtype=tf.complex128)
    return tf.linalg.adjoint(B) @ U @ B


# TODO - super_to_choi is not compatible with tf.function
def super_to_choi(A):
    """
    Convert a super operator to choi representation.

    """
    sqrt_shape = int(np.sqrt(A.shape[0]))
    A_choi = tf.reshape(
        tf.transpose(tf.reshape(A, [sqrt_shape] * 4), perm=[3, 1, 2, 0]), tf.shape(A)
    )
    return A_choi


def tf_project_to_comp(A, dims, index=None, to_super=False):
    """Project an operator onto the computational subspace."""
    if not index:
        index = list(range(len(dims)))
    proj = projector(dims, index)
    if to_super:
        proj = np.kron(proj, proj)
    P = tf.constant(proj, dtype=A.dtype)
    return tf.matmul(tf.matmul(P, A, transpose_a=True), P)


def tf_convolve(sig: tf.Tensor, resp: tf.Tensor):
    """
    Compute the convolution with a time response.

    Parameters
    ----------
    sig : tf.Tensor
        Signal which will be convoluted, shape: [N]
    resp : tf.Tensor
        Response function to be convoluted with signal, shape: [M]

    Returns
    -------
    tf.Tensor
        convoluted signal of shape [N]

    """
    sig = tf.cast(sig, dtype=tf.complex128)
    resp = tf.cast(resp, dtype=tf.complex128)

    sig_len = len(sig)
    resp_len = len(resp)

    signal_pad = tf.expand_dims(
        tf.concat([sig, tf.zeros(resp_len, dtype=tf.complex128)], axis=0), 0
    )
    resp_pad = tf.expand_dims(
        tf.concat([resp, tf.zeros(sig_len, dtype=tf.complex128)], axis=0), 0
    )
    sig_resp = tf.concat([signal_pad, resp_pad], axis=0)

    fft_sig_resp = tf.signal.fft(sig_resp)
    fft_conv = tf.math.reduce_prod(fft_sig_resp, axis=0)
    convolution = tf.signal.ifft(fft_conv)
    return convolution[:sig_len]


def tf_convolve_legacy(sig: tf.Tensor, resp: tf.Tensor):
    """
    Compute the convolution with a time response. LEGACY version. Ensures compatibility with the previous response implementation.

    Parameters
    ----------
    sig : tf.Tensor
        Signal which will be convoluted, shape: [N]
    resp : tf.Tensor
        Response function to be convoluted with signal, shape: [M]

    Returns
    -------
    tf.Tensor
        convoluted signal of shape [N]

    """
    sig = tf.cast(sig, dtype=tf.complex128)
    resp = tf.cast(resp, dtype=tf.complex128)

    sig_len = len(sig)
    resp_len = len(resp)

    signal_pad = tf.expand_dims(
        tf.concat(
            [
                tf.zeros(resp_len, dtype=tf.complex128),
                sig,
                tf.zeros(resp_len, dtype=tf.complex128),
            ],
            axis=0,
        ),
        0,
    )
    resp_pad = tf.expand_dims(
        tf.concat([resp, tf.zeros(sig_len + resp_len, dtype=tf.complex128)], axis=0), 0
    )
    sig_resp = tf.concat([signal_pad, resp_pad], axis=0)

    fft_sig_resp = tf.signal.fft(sig_resp)
    fft_conv = tf.math.reduce_prod(fft_sig_resp, axis=0)
    convolution = tf.signal.ifft(fft_conv)
    return convolution[resp_len - 1 : sig_len + resp_len - 1]


def interpolate_signal(ts, sig, interpolate_res):
    dt = ts[1] - ts[0]
    if interpolate_res == -1:  # DOPRI5
        ts = tf.cast(ts, dtype=tf.float64)
        dt = ts[1] - ts[0]
        ts_interp = tf.concat(
            [
                ts,
                ts + 1.0 / 5 * dt,
                ts + 3.0 / 10 * dt,
                ts + 4.0 / 5 * dt,
                ts + 8.0 / 9 * dt,
                ts + dt,
            ],
            axis=0,
        )
        ts_interp = tf.sort(ts_interp)
    elif interpolate_res == -2:  # tsit5
        ts = tf.cast(ts, dtype=tf.float64)
        dt = ts[1] - ts[0]
        ts_interp = tf.concat(
            [
                ts,
                ts + 0.161 * dt,
                ts + 0.327 * dt,
                ts + 0.9 * dt,
                ts + 0.9800255409045097 * dt,
                ts + dt,
            ],
            axis=0,
        )
        ts_interp = tf.sort(ts_interp)
    else:
        ts_interp = tf.linspace(
            ts[0], ts[-1] + dt, tf.shape(ts)[0] * interpolate_res + 1
        )
    return tfp.math.interp_regular_1d_grid(
        ts_interp, ts[0], ts[-1], sig, fill_value="extrapolate"
    )


def commutator(A, B):
    return tf.matmul(A, B) - tf.matmul(B, A)


def anticommutator(A, B):
    return tf.matmul(A, B) + tf.matmul(B, A)
