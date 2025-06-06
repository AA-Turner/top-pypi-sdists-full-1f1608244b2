#cython: boundscheck=False
#cython: wraparound=False
#cython: cdivision=False
"""
State Space Models

Author: Chad Fulton  
License: Simplified-BSD

Notes
-----

The dimensions used in all the BLAS / LAPACK calls below use the following
convention:

- The dimensions of the arrays *as they are to be manipulated* are all defined
  as model._k_*
- If the array in question is defined in the Statespace object
  (obs, obs_intercept, design, obs_cov, state_intercept, transition, selection,
  state_cov, selected_state_cov), then the dimension in-memory is defined as
  model._k_*
  This is because the in-memory shape of matrices changes according to whether
  or not data is missing and whether or not the generalized collapse transform
  is applied.
- If the array in question is defined in the Kalman filter object
  (forecast_*, filtered_*, predicted_*, etc.), then the dimension in-memory is
  defined as kfilter.k_*
  This is because the in-memory shape of matrices only changes according to
  filter_method.
- If the array in question is defined in the Kalman smoother object
  (smoothed_*, etc.), then the dimension in-memory is defined as kfilter.k_*
  This is because the in-memory shape of matrices only changes according to
  filter_method.

Thus, for example, a ?gemm call has the following signature:

dgemm(transa, transb, m, n, k, alpha, a, lda, b, ldb, beta, c, ldc)

- m, n, and k are the dimensions *as they are to be manipulated*, and are
  always defined as model._k_*
- lda, ldb, and ldc are the *in-memory* dimension, and they are set as
  model._k_* if the array is defined in the Statespace object, otherwise
  (in either the filter or smoother cases) they are set as kfilter.k_*

Note that for ?copy calls, the number of elements to be copied is defined to be
the dimension in memory of the array that is being copied *from*.
"""

# Typical imports
import numpy as np
cimport numpy as np
from statsmodels.src.math cimport *
cimport scipy.linalg.cython_blas as blas

from statsmodels.tsa.statespace._kalman_smoother cimport (
    SMOOTHER_STATE, SMOOTHER_STATE_COV, SMOOTHER_DISTURBANCE,
    SMOOTHER_DISTURBANCE_COV
)

# ### Missing Observation Conventional Kalman smoother
#
# See Durbin and Koopman (2012) Chapter 4.10
#
# Here k_endog is the same as usual, but the design matrix and observation
# covariance matrix are enforced to be zero matrices.

cdef int ssmoothed_estimators_missing_conventional(sKalmanSmoother smoother, sKalmanFilter kfilter, sStatespace model) except *:
    cdef:
        int inc = 1
        np.float32_t alpha = 1.0
        np.float32_t beta = 0.0
        np.float32_t gamma = -1.0

    # Scaled smoothed estimator  
    # $r_{t-1} = T_t' r_t$  
    # $(m \times 1) = (m \times m) (m \times 1)$
    # Note: save $r_{t-1}$ as scaled_smoothed_estimator[t] rather than
    # as scaled_smoothed_estimator[t-1] because we actually need to store
    # T+1 of them (r_{T-1} to r_{-1} -> r_T to r_0)
    if smoother.smoother_output & (SMOOTHER_STATE | SMOOTHER_DISTURBANCE):
        if model.identity_transition:
            blas.scopy(&model._k_states, smoother._input_scaled_smoothed_estimator, &inc, smoother._scaled_smoothed_estimator, &inc)
        else:
            blas.sgemv("T", &model._k_states, &model._k_states,
                    &alpha, model._transition, &model._k_states,
                            smoother._input_scaled_smoothed_estimator, &inc,
                    &beta, smoother._scaled_smoothed_estimator, &inc)

    # Scaled smoothed estimator covariance matrix  
    # $N_{t-1} = T_t' N_t T_t$  
    # $(m \times m) = (m \times m) (m \times m) (m \times m)$  
    # Note: save $N_{t-1}$ as scaled_smoothed_estimator_cov[t] rather
    # than as scaled_smoothed_estimator_cov[t-1] because we actually
    # need to store T+1 of them (N_{T-1} to N_{-1} -> N_T to N_0)
    if smoother.smoother_output & (SMOOTHER_STATE_COV | SMOOTHER_DISTURBANCE_COV):
        if model.identity_transition:
            blas.scopy(&model._k_states2, smoother._input_scaled_smoothed_estimator_cov, &inc, smoother._scaled_smoothed_estimator_cov, &inc)
        else:
            blas.sgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
                      &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                              model._transition, &model._k_states,
                      &beta, smoother._tmp0, &kfilter.k_states)
            blas.sgemm("T", "N", &kfilter.k_states, &kfilter.k_states, &kfilter.k_states,
                      &alpha, model._transition, &model._k_states,
                              smoother._tmp0, &kfilter.k_states,
                      &beta, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states)

    # $L_t = T_t$  
    blas.scopy(&model._k_states2, model._transition, &inc, smoother._tmpL, &inc)

    # Smoothing error  
    # It is undefined here, since F_t^{-1} is nan
    # for i in range(kfilter.k_endog):
    #     smoother._smoothing_error[i] = 0

    # Smoothing error  
    # $u_t = - K_t' r_t$  
    # $(p \times 1) = (p \times 1) - (p \times m) (m \times 1)$  
    # TODO in the missing case, I think K_t is defined to be zeros, so this
    # would be unnecessary
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE):
        blas.sgemv("T", &model._k_states, &model._k_endog,
                  &gamma, kfilter._kalman_gain, &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator, &inc,
                  &beta, smoother._smoothing_error, &inc)

cdef int ssmoothed_disturbances_missing_conventional(sKalmanSmoother smoother, sKalmanFilter kfilter, sStatespace model):
    cdef:
        int inc = 1
        np.float32_t alpha = 1.0
        np.float32_t beta = 0.0
        np.float32_t gamma = -1.0

    # Temporary arrays

    # $\\#_0 = R_t Q_t$  
    # $(m \times r) = (m \times r) (r \times r)$
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE | SMOOTHER_DISTURBANCE_COV):
        blas.sgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_posdef,
                  &alpha, model._selection, &model._k_states,
                          model._state_cov, &model._k_posdef,
                  &beta, smoother._tmp0, &kfilter.k_states)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE:
        # Smoothed state disturbance  
        # $\hat \eta_t = \\#_0' r_t$  
        # $(r \times 1) = (r \times m) (m \times 1)$  
        blas.sgemv("T", &kfilter.k_states, &kfilter.k_posdef,
                      &alpha, smoother._tmp0, &kfilter.k_states,
                              smoother._input_scaled_smoothed_estimator, &inc,
                      &beta, smoother._smoothed_state_disturbance, &inc)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE_COV:
      # Smoothed state disturbance covariance matrix  
        # $Var(\eta_t | Y_n) = Q_t - \\#_0' N_t \\#_0$  
        # $(r \times r) = (r \times r) - (r \times m) (m \times m) (m \times r)$  
        blas.sgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmp0, &kfilter.k_states,
                  &beta, smoother._tmpL, &kfilter.k_states)
        blas.scopy(&model._k_posdef2, model._state_cov, &inc, smoother._smoothed_state_disturbance_cov, &inc)
        blas.sgemm("T", "N", &model._k_posdef, &model._k_posdef, &model._k_states,
                  &gamma, smoother._tmp0, &kfilter.k_states,
                          smoother._tmpL, &kfilter.k_states,
                  &alpha, smoother._smoothed_state_disturbance_cov, &kfilter.k_posdef)


    # Just return the unconditional distribution for the measurement
    # disturbances corresponding to a missing observation

    # TODO this is not explicitly addressed in Durbin and Koopman Chapter 4
    # or in Koopman (1993) - need to find a source for if this is correct
    # Note: this is what the MATLAB ssm toolbox does, also

    # Smoothed measurement disturbances have unconditional expected
    # value of 0, so no need to do anything

    # Smoothed measurement and state disturbances have unconditional covariance
    # matrix of $H_t, Q_t$, respectively
    blas.scopy(&model._k_endog2, model._obs_cov, &inc, smoother._smoothed_measurement_disturbance_cov, &inc)


# ### Conventional Kalman smoother
#
# The following are the above routines as defined in the conventional Kalman
# smoother.
#
# See Durbin and Koopman (2012) Chapter 4

cdef int ssmoothed_estimators_measurement_conventional(sKalmanSmoother smoother, sKalmanFilter kfilter, sStatespace model) except *:
    cdef:
        int i
        int inc = 1
        np.float32_t alpha = 1.0
        np.float32_t beta = 0.0
        np.float32_t gamma = -1.0

    # Smoothing error  
    # $u_t = \\#_2 - K_t' r_t$  
    # $(p \times 1) = (p \times 1) - (p \times m) (m \times 1)$ 
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE):
        blas.scopy(&model._k_endog, kfilter._tmp2, &inc, smoother._smoothing_error, &inc)
        blas.sgemv("T", &model._k_states, &model._k_endog,
                  &gamma, kfilter._kalman_gain, &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator, &inc,
                  &alpha, smoother._smoothing_error, &inc)

    # $L_t = (T_t - K_t Z_t)$  = (T_t - T_t P_t Z_t' F_t^{-1} Z_t)
    # $(m \times m) = (m \times m) + (m \times p) (p \times m)$
    # (this is required for any type of smoothing)
    blas.scopy(&model._k_states2, model._transition, &inc, smoother._tmpL, &inc)
    blas.sgemm("N", "N", &model._k_states, &model._k_states, &model._k_endog,
              &gamma, kfilter._kalman_gain, &kfilter.k_states,
                      model._design, &model._k_endog,
              &alpha, smoother._tmpL, &kfilter.k_states)

    # Scaled smoothed estimator  
    # $r_{t-1} = Z_t' \\#_2 + L_t' r_t$  
    # $(m \times 1) = (m \times p) (p \times 1) + (m \times m) (m \times 1)$
    # Note: save $r_{t-1}$ as scaled_smoothed_estimator[t] rather than
    # as scaled_smoothed_estimator[t-1] because we actually need to store
    # T+1 of them (r_{T-1} to r_{-1} -> r_T to r_0)
    if smoother.smoother_output & (SMOOTHER_STATE | SMOOTHER_DISTURBANCE):
        blas.sgemv("T", &model._k_states, &model._k_states,
                  &alpha, smoother._tmpL, &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator, &inc,
                  &beta, smoother._scaled_smoothed_estimator, &inc)

        blas.sgemv("T", &model._k_endog, &model._k_states,
                  &alpha, model._design, &model._k_endog,
                          kfilter._tmp2, &inc,
                  &alpha, smoother._scaled_smoothed_estimator, &inc)

    # Scaled smoothed estimator covariance matrix  
    # $N_{t-1} = Z_t' \\#_3 + L_t' N_t L_t$  
    # $(m \times m) = (m \times p) (p \times m) + (m \times m) (m \times m) (m \times m)$  
    # Note: save $N_{t-1}$ as scaled_smoothed_estimator_cov[t] rather
    # than as scaled_smoothed_estimator_cov[t-1] because we actually
    # need to store T+1 of them (N_{T-1} to N_{-1} -> N_T to N_0)
    if smoother.smoother_output & (SMOOTHER_STATE_COV | SMOOTHER_DISTURBANCE_COV):
        blas.sgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmpL, &kfilter.k_states,
                  &beta, smoother._tmp0, &kfilter.k_states)
        blas.sgemm("T", "N", &model._k_states, &model._k_states, &model._k_states,
                  &alpha, smoother._tmpL, &kfilter.k_states,
                          smoother._tmp0, &kfilter.k_states,
                  &beta, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states)
        blas.sgemm("T", "N", &model._k_states, &model._k_states, &model._k_endog,
                  &alpha, model._design, &model._k_endog,
                          kfilter._tmp3, &kfilter.k_endog,
                  &alpha, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states)

cdef int ssmoothed_estimators_time_conventional(sKalmanSmoother smoother, sKalmanFilter kfilter, sStatespace model):
  pass

cdef int ssmoothed_state_conventional(sKalmanSmoother smoother, sKalmanFilter kfilter, sStatespace model):
    cdef int i, j
    cdef:
        int inc = 1
        np.float32_t alpha = 1.0
        np.float32_t beta = 0.0
        np.float32_t gamma = -1.0

    # Smoothed state
    if smoother.smoother_output & SMOOTHER_STATE:
        # $\hat \alpha_t = a_t + P_t r_{t-1}$  
        # $(m \times 1) = (m \times 1) + (m \times m) (m \times 1)$  
        blas.scopy(&kfilter.k_states, &kfilter.predicted_state[0,smoother.t], &inc, smoother._smoothed_state, &inc)
        blas.sgemv("N", &model._k_states, &model._k_states,
                  &alpha, &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
                          smoother._scaled_smoothed_estimator, &inc,
                  &alpha, smoother._smoothed_state, &inc)

    # Smoothed state covariance
    if smoother.smoother_output & SMOOTHER_STATE_COV:
        # $V_t = P_t [I - N_{t-1} P_t]$  
        # $(m \times m) = (m \times m) [(m \times m) - (m \times m) (m \times m)]$  
        blas.sgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
              &gamma, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states,
                      &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
              &beta, smoother._tmp0, &kfilter.k_states)
        for i in range(kfilter.k_states):
            smoother.tmp0[i,i] = 1 + smoother.tmp0[i,i]
        blas.sgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
              &alpha, &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
                      smoother._tmp0, &kfilter.k_states,
              &beta, smoother._smoothed_state_cov, &kfilter.k_states)


cdef int ssmoothed_state_autocov_conventional(sKalmanSmoother smoother, sKalmanFilter kfilter, sStatespace model):
    cdef:
        int i
        int inc = 1
        np.float32_t alpha = 1.0
        np.float32_t beta = 0.0
        np.float32_t gamma = -1.0
    # This function computes Cov(alpha_{t+1}, alpha_t) = Cov(alpha_t, alpha_{t+1})'
    # From Durbin and Koopman, 2012, Chapter 4.7
    # Cov(alpha_{t+1}, alpha_t) = (I - P_{t+1} N_{t}) L_t P_t

    blas.sgemm("N", "N", &model.k_states, &model.k_states, &model.k_states,
                  &gamma, &kfilter.predicted_state_cov[0,0,smoother.t+1], &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                  &beta, smoother._tmp0, &kfilter.k_states)
    for i in range(kfilter.k_states):
        smoother.tmp0[i,i] = 1 + smoother.tmp0[i,i]

    blas.sgemm("N", "N", &model.k_states, &model.k_states, &model.k_states,
                  &alpha, smoother._tmpL, &kfilter.k_states,
                          &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
                  &beta, smoother._tmp_autocov, &kfilter.k_states)

    blas.sgemm("N", "N", &model.k_states, &model.k_states, &model.k_states,
                  &alpha, smoother._tmp0, &kfilter.k_states,
                          smoother._tmp_autocov, &kfilter.k_states,
                  &beta, smoother._smoothed_state_autocov, &kfilter.k_states)

cdef int ssmoothed_disturbances_conventional(sKalmanSmoother smoother, sKalmanFilter kfilter, sStatespace model):
    cdef int i, j
    cdef:
        int inc = 1
        np.float32_t alpha = 1.0
        np.float32_t beta = 0.0
        np.float32_t gamma = -1.0

    # Temporary arrays

    # $\\#_0 = R_t Q_t$  
    # $(m \times r) = (m \times r) (r \times r)$
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE | SMOOTHER_DISTURBANCE_COV):
        blas.sgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_posdef,
                  &alpha, model._selection, &model._k_states,
                          model._state_cov, &model._k_posdef,
                  &beta, smoother._tmp0, &kfilter.k_states)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE:
        # Smoothed measurement disturbance  
        # $\hat \varepsilon_t = H_t u_t$  
        # $(p \times 1) = (p \times p) (p \times 1)$  
        blas.sgemv("N", &model._k_endog, &model._k_endog,
                      &alpha, model._obs_cov, &model._k_endog,
                              smoother._smoothing_error, &inc,
                      &beta, smoother._smoothed_measurement_disturbance, &inc)

        # Smoothed state disturbance  
        # $\hat \eta_t = \\#_0' r_t$  
        # $(r \times 1) = (r \times m) (m \times 1)$  
        blas.sgemv("T", &model._k_states, &model._k_posdef,
                      &alpha, smoother._tmp0, &kfilter.k_states,
                              smoother._input_scaled_smoothed_estimator, &inc,
                      &beta, smoother._smoothed_state_disturbance, &inc)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE_COV:
        # $\\#_00 = K_t H_t$  
        # $(m \times p) = (m \times p) (p \times p)$  
        blas.sgemm("N", "N", &model._k_states, &model._k_endog, &model._k_endog,
                  &alpha, kfilter._kalman_gain, &kfilter.k_states,
                          model._obs_cov, &model._k_endog,
                  &beta, smoother._tmp00, &kfilter.k_states)

        # Smoothed measurement disturbance covariance matrix  
        # $Var(\varepsilon_t | Y_n) = H_t - H_t \\#_4 - \\#_00' N_t \\#_00$  
        # $(p \times p) = (p \times p) - (p \times p) (p \times p) - (p \times m) (m \times m) (m \times p)$  
        blas.sgemm("N", "N", &model._k_endog, &model._k_endog, &model._k_endog,
                  &gamma, model._obs_cov, &model._k_endog,
                          kfilter._tmp4, &kfilter.k_endog,
                  &beta, smoother._smoothed_measurement_disturbance_cov, &kfilter.k_endog)

        blas.sgemm("N", "N", &model._k_states, &model._k_endog, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmp00, &kfilter.k_states,
                  &beta, smoother._tmp000, &kfilter.k_states)

        blas.sgemm("T", "N", &model._k_endog, &model._k_endog, &model._k_states,
                  &gamma, smoother._tmp00, &kfilter.k_states,
                          smoother._tmp000, &kfilter.k_states,
                  &alpha, smoother._smoothed_measurement_disturbance_cov, &kfilter.k_endog)

        # blas.saxpy(&model._k_endog2, &alpha,
        #        model._obs_cov, &inc,
        #        smoother._smoothed_measurement_disturbance_cov, &inc)
        for i in range(kfilter.k_endog):
            for j in range(i+1):
                smoother._smoothed_measurement_disturbance_cov[i + j*kfilter.k_endog] = model._obs_cov[i + j*model._k_endog] + smoother._smoothed_measurement_disturbance_cov[i + j*kfilter.k_endog]
                if not i == j:
                    smoother._smoothed_measurement_disturbance_cov[j + i*kfilter.k_endog] = model._obs_cov[j + i*model._k_endog] + smoother._smoothed_measurement_disturbance_cov[j + i*kfilter.k_endog]
        
        # Smoothed state disturbance covariance matrix  
        # $Var(\eta_t | Y_n) = Q_t - \\#_0' N_t \\#_0$  
        # $(r \times r) = (r \times r) - (r \times m) (m \times m) (m \times r)$  
        blas.sgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmp0, &kfilter.k_states,
                  &beta, smoother._tmpL, &kfilter.k_states)

        blas.scopy(&model._k_posdef2, model._state_cov, &inc, smoother._smoothed_state_disturbance_cov, &inc)
        blas.sgemm("T", "N", &model._k_posdef, &model._k_posdef, &model._k_states,
                  &gamma, smoother._tmp0, &kfilter.k_states,
                          smoother._tmpL, &kfilter.k_states,
                  &alpha, smoother._smoothed_state_disturbance_cov, &kfilter.k_posdef)

# ### Missing Observation Conventional Kalman smoother
#
# See Durbin and Koopman (2012) Chapter 4.10
#
# Here k_endog is the same as usual, but the design matrix and observation
# covariance matrix are enforced to be zero matrices.

cdef int dsmoothed_estimators_missing_conventional(dKalmanSmoother smoother, dKalmanFilter kfilter, dStatespace model) except *:
    cdef:
        int inc = 1
        np.float64_t alpha = 1.0
        np.float64_t beta = 0.0
        np.float64_t gamma = -1.0

    # Scaled smoothed estimator  
    # $r_{t-1} = T_t' r_t$  
    # $(m \times 1) = (m \times m) (m \times 1)$
    # Note: save $r_{t-1}$ as scaled_smoothed_estimator[t] rather than
    # as scaled_smoothed_estimator[t-1] because we actually need to store
    # T+1 of them (r_{T-1} to r_{-1} -> r_T to r_0)
    if smoother.smoother_output & (SMOOTHER_STATE | SMOOTHER_DISTURBANCE):
        if model.identity_transition:
            blas.dcopy(&model._k_states, smoother._input_scaled_smoothed_estimator, &inc, smoother._scaled_smoothed_estimator, &inc)
        else:
            blas.dgemv("T", &model._k_states, &model._k_states,
                    &alpha, model._transition, &model._k_states,
                            smoother._input_scaled_smoothed_estimator, &inc,
                    &beta, smoother._scaled_smoothed_estimator, &inc)

    # Scaled smoothed estimator covariance matrix  
    # $N_{t-1} = T_t' N_t T_t$  
    # $(m \times m) = (m \times m) (m \times m) (m \times m)$  
    # Note: save $N_{t-1}$ as scaled_smoothed_estimator_cov[t] rather
    # than as scaled_smoothed_estimator_cov[t-1] because we actually
    # need to store T+1 of them (N_{T-1} to N_{-1} -> N_T to N_0)
    if smoother.smoother_output & (SMOOTHER_STATE_COV | SMOOTHER_DISTURBANCE_COV):
        if model.identity_transition:
            blas.dcopy(&model._k_states2, smoother._input_scaled_smoothed_estimator_cov, &inc, smoother._scaled_smoothed_estimator_cov, &inc)
        else:
            blas.dgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
                      &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                              model._transition, &model._k_states,
                      &beta, smoother._tmp0, &kfilter.k_states)
            blas.dgemm("T", "N", &kfilter.k_states, &kfilter.k_states, &kfilter.k_states,
                      &alpha, model._transition, &model._k_states,
                              smoother._tmp0, &kfilter.k_states,
                      &beta, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states)

    # $L_t = T_t$  
    blas.dcopy(&model._k_states2, model._transition, &inc, smoother._tmpL, &inc)

    # Smoothing error  
    # It is undefined here, since F_t^{-1} is nan
    # for i in range(kfilter.k_endog):
    #     smoother._smoothing_error[i] = 0

    # Smoothing error  
    # $u_t = - K_t' r_t$  
    # $(p \times 1) = (p \times 1) - (p \times m) (m \times 1)$  
    # TODO in the missing case, I think K_t is defined to be zeros, so this
    # would be unnecessary
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE):
        blas.dgemv("T", &model._k_states, &model._k_endog,
                  &gamma, kfilter._kalman_gain, &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator, &inc,
                  &beta, smoother._smoothing_error, &inc)

cdef int dsmoothed_disturbances_missing_conventional(dKalmanSmoother smoother, dKalmanFilter kfilter, dStatespace model):
    cdef:
        int inc = 1
        np.float64_t alpha = 1.0
        np.float64_t beta = 0.0
        np.float64_t gamma = -1.0

    # Temporary arrays

    # $\\#_0 = R_t Q_t$  
    # $(m \times r) = (m \times r) (r \times r)$
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE | SMOOTHER_DISTURBANCE_COV):
        blas.dgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_posdef,
                  &alpha, model._selection, &model._k_states,
                          model._state_cov, &model._k_posdef,
                  &beta, smoother._tmp0, &kfilter.k_states)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE:
        # Smoothed state disturbance  
        # $\hat \eta_t = \\#_0' r_t$  
        # $(r \times 1) = (r \times m) (m \times 1)$  
        blas.dgemv("T", &kfilter.k_states, &kfilter.k_posdef,
                      &alpha, smoother._tmp0, &kfilter.k_states,
                              smoother._input_scaled_smoothed_estimator, &inc,
                      &beta, smoother._smoothed_state_disturbance, &inc)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE_COV:
      # Smoothed state disturbance covariance matrix  
        # $Var(\eta_t | Y_n) = Q_t - \\#_0' N_t \\#_0$  
        # $(r \times r) = (r \times r) - (r \times m) (m \times m) (m \times r)$  
        blas.dgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmp0, &kfilter.k_states,
                  &beta, smoother._tmpL, &kfilter.k_states)
        blas.dcopy(&model._k_posdef2, model._state_cov, &inc, smoother._smoothed_state_disturbance_cov, &inc)
        blas.dgemm("T", "N", &model._k_posdef, &model._k_posdef, &model._k_states,
                  &gamma, smoother._tmp0, &kfilter.k_states,
                          smoother._tmpL, &kfilter.k_states,
                  &alpha, smoother._smoothed_state_disturbance_cov, &kfilter.k_posdef)


    # Just return the unconditional distribution for the measurement
    # disturbances corresponding to a missing observation

    # TODO this is not explicitly addressed in Durbin and Koopman Chapter 4
    # or in Koopman (1993) - need to find a source for if this is correct
    # Note: this is what the MATLAB ssm toolbox does, also

    # Smoothed measurement disturbances have unconditional expected
    # value of 0, so no need to do anything

    # Smoothed measurement and state disturbances have unconditional covariance
    # matrix of $H_t, Q_t$, respectively
    blas.dcopy(&model._k_endog2, model._obs_cov, &inc, smoother._smoothed_measurement_disturbance_cov, &inc)


# ### Conventional Kalman smoother
#
# The following are the above routines as defined in the conventional Kalman
# smoother.
#
# See Durbin and Koopman (2012) Chapter 4

cdef int dsmoothed_estimators_measurement_conventional(dKalmanSmoother smoother, dKalmanFilter kfilter, dStatespace model) except *:
    cdef:
        int i
        int inc = 1
        np.float64_t alpha = 1.0
        np.float64_t beta = 0.0
        np.float64_t gamma = -1.0

    # Smoothing error  
    # $u_t = \\#_2 - K_t' r_t$  
    # $(p \times 1) = (p \times 1) - (p \times m) (m \times 1)$ 
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE):
        blas.dcopy(&model._k_endog, kfilter._tmp2, &inc, smoother._smoothing_error, &inc)
        blas.dgemv("T", &model._k_states, &model._k_endog,
                  &gamma, kfilter._kalman_gain, &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator, &inc,
                  &alpha, smoother._smoothing_error, &inc)

    # $L_t = (T_t - K_t Z_t)$  = (T_t - T_t P_t Z_t' F_t^{-1} Z_t)
    # $(m \times m) = (m \times m) + (m \times p) (p \times m)$
    # (this is required for any type of smoothing)
    blas.dcopy(&model._k_states2, model._transition, &inc, smoother._tmpL, &inc)
    blas.dgemm("N", "N", &model._k_states, &model._k_states, &model._k_endog,
              &gamma, kfilter._kalman_gain, &kfilter.k_states,
                      model._design, &model._k_endog,
              &alpha, smoother._tmpL, &kfilter.k_states)

    # Scaled smoothed estimator  
    # $r_{t-1} = Z_t' \\#_2 + L_t' r_t$  
    # $(m \times 1) = (m \times p) (p \times 1) + (m \times m) (m \times 1)$
    # Note: save $r_{t-1}$ as scaled_smoothed_estimator[t] rather than
    # as scaled_smoothed_estimator[t-1] because we actually need to store
    # T+1 of them (r_{T-1} to r_{-1} -> r_T to r_0)
    if smoother.smoother_output & (SMOOTHER_STATE | SMOOTHER_DISTURBANCE):
        blas.dgemv("T", &model._k_states, &model._k_states,
                  &alpha, smoother._tmpL, &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator, &inc,
                  &beta, smoother._scaled_smoothed_estimator, &inc)

        blas.dgemv("T", &model._k_endog, &model._k_states,
                  &alpha, model._design, &model._k_endog,
                          kfilter._tmp2, &inc,
                  &alpha, smoother._scaled_smoothed_estimator, &inc)

    # Scaled smoothed estimator covariance matrix  
    # $N_{t-1} = Z_t' \\#_3 + L_t' N_t L_t$  
    # $(m \times m) = (m \times p) (p \times m) + (m \times m) (m \times m) (m \times m)$  
    # Note: save $N_{t-1}$ as scaled_smoothed_estimator_cov[t] rather
    # than as scaled_smoothed_estimator_cov[t-1] because we actually
    # need to store T+1 of them (N_{T-1} to N_{-1} -> N_T to N_0)
    if smoother.smoother_output & (SMOOTHER_STATE_COV | SMOOTHER_DISTURBANCE_COV):
        blas.dgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmpL, &kfilter.k_states,
                  &beta, smoother._tmp0, &kfilter.k_states)
        blas.dgemm("T", "N", &model._k_states, &model._k_states, &model._k_states,
                  &alpha, smoother._tmpL, &kfilter.k_states,
                          smoother._tmp0, &kfilter.k_states,
                  &beta, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states)
        blas.dgemm("T", "N", &model._k_states, &model._k_states, &model._k_endog,
                  &alpha, model._design, &model._k_endog,
                          kfilter._tmp3, &kfilter.k_endog,
                  &alpha, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states)

cdef int dsmoothed_estimators_time_conventional(dKalmanSmoother smoother, dKalmanFilter kfilter, dStatespace model):
  pass

cdef int dsmoothed_state_conventional(dKalmanSmoother smoother, dKalmanFilter kfilter, dStatespace model):
    cdef int i, j
    cdef:
        int inc = 1
        np.float64_t alpha = 1.0
        np.float64_t beta = 0.0
        np.float64_t gamma = -1.0

    # Smoothed state
    if smoother.smoother_output & SMOOTHER_STATE:
        # $\hat \alpha_t = a_t + P_t r_{t-1}$  
        # $(m \times 1) = (m \times 1) + (m \times m) (m \times 1)$  
        blas.dcopy(&kfilter.k_states, &kfilter.predicted_state[0,smoother.t], &inc, smoother._smoothed_state, &inc)
        blas.dgemv("N", &model._k_states, &model._k_states,
                  &alpha, &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
                          smoother._scaled_smoothed_estimator, &inc,
                  &alpha, smoother._smoothed_state, &inc)

    # Smoothed state covariance
    if smoother.smoother_output & SMOOTHER_STATE_COV:
        # $V_t = P_t [I - N_{t-1} P_t]$  
        # $(m \times m) = (m \times m) [(m \times m) - (m \times m) (m \times m)]$  
        blas.dgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
              &gamma, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states,
                      &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
              &beta, smoother._tmp0, &kfilter.k_states)
        for i in range(kfilter.k_states):
            smoother.tmp0[i,i] = 1 + smoother.tmp0[i,i]
        blas.dgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
              &alpha, &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
                      smoother._tmp0, &kfilter.k_states,
              &beta, smoother._smoothed_state_cov, &kfilter.k_states)


cdef int dsmoothed_state_autocov_conventional(dKalmanSmoother smoother, dKalmanFilter kfilter, dStatespace model):
    cdef:
        int i
        int inc = 1
        np.float64_t alpha = 1.0
        np.float64_t beta = 0.0
        np.float64_t gamma = -1.0
    # This function computes Cov(alpha_{t+1}, alpha_t) = Cov(alpha_t, alpha_{t+1})'
    # From Durbin and Koopman, 2012, Chapter 4.7
    # Cov(alpha_{t+1}, alpha_t) = (I - P_{t+1} N_{t}) L_t P_t

    blas.dgemm("N", "N", &model.k_states, &model.k_states, &model.k_states,
                  &gamma, &kfilter.predicted_state_cov[0,0,smoother.t+1], &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                  &beta, smoother._tmp0, &kfilter.k_states)
    for i in range(kfilter.k_states):
        smoother.tmp0[i,i] = 1 + smoother.tmp0[i,i]

    blas.dgemm("N", "N", &model.k_states, &model.k_states, &model.k_states,
                  &alpha, smoother._tmpL, &kfilter.k_states,
                          &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
                  &beta, smoother._tmp_autocov, &kfilter.k_states)

    blas.dgemm("N", "N", &model.k_states, &model.k_states, &model.k_states,
                  &alpha, smoother._tmp0, &kfilter.k_states,
                          smoother._tmp_autocov, &kfilter.k_states,
                  &beta, smoother._smoothed_state_autocov, &kfilter.k_states)

cdef int dsmoothed_disturbances_conventional(dKalmanSmoother smoother, dKalmanFilter kfilter, dStatespace model):
    cdef int i, j
    cdef:
        int inc = 1
        np.float64_t alpha = 1.0
        np.float64_t beta = 0.0
        np.float64_t gamma = -1.0

    # Temporary arrays

    # $\\#_0 = R_t Q_t$  
    # $(m \times r) = (m \times r) (r \times r)$
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE | SMOOTHER_DISTURBANCE_COV):
        blas.dgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_posdef,
                  &alpha, model._selection, &model._k_states,
                          model._state_cov, &model._k_posdef,
                  &beta, smoother._tmp0, &kfilter.k_states)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE:
        # Smoothed measurement disturbance  
        # $\hat \varepsilon_t = H_t u_t$  
        # $(p \times 1) = (p \times p) (p \times 1)$  
        blas.dgemv("N", &model._k_endog, &model._k_endog,
                      &alpha, model._obs_cov, &model._k_endog,
                              smoother._smoothing_error, &inc,
                      &beta, smoother._smoothed_measurement_disturbance, &inc)

        # Smoothed state disturbance  
        # $\hat \eta_t = \\#_0' r_t$  
        # $(r \times 1) = (r \times m) (m \times 1)$  
        blas.dgemv("T", &model._k_states, &model._k_posdef,
                      &alpha, smoother._tmp0, &kfilter.k_states,
                              smoother._input_scaled_smoothed_estimator, &inc,
                      &beta, smoother._smoothed_state_disturbance, &inc)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE_COV:
        # $\\#_00 = K_t H_t$  
        # $(m \times p) = (m \times p) (p \times p)$  
        blas.dgemm("N", "N", &model._k_states, &model._k_endog, &model._k_endog,
                  &alpha, kfilter._kalman_gain, &kfilter.k_states,
                          model._obs_cov, &model._k_endog,
                  &beta, smoother._tmp00, &kfilter.k_states)

        # Smoothed measurement disturbance covariance matrix  
        # $Var(\varepsilon_t | Y_n) = H_t - H_t \\#_4 - \\#_00' N_t \\#_00$  
        # $(p \times p) = (p \times p) - (p \times p) (p \times p) - (p \times m) (m \times m) (m \times p)$  
        blas.dgemm("N", "N", &model._k_endog, &model._k_endog, &model._k_endog,
                  &gamma, model._obs_cov, &model._k_endog,
                          kfilter._tmp4, &kfilter.k_endog,
                  &beta, smoother._smoothed_measurement_disturbance_cov, &kfilter.k_endog)

        blas.dgemm("N", "N", &model._k_states, &model._k_endog, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmp00, &kfilter.k_states,
                  &beta, smoother._tmp000, &kfilter.k_states)

        blas.dgemm("T", "N", &model._k_endog, &model._k_endog, &model._k_states,
                  &gamma, smoother._tmp00, &kfilter.k_states,
                          smoother._tmp000, &kfilter.k_states,
                  &alpha, smoother._smoothed_measurement_disturbance_cov, &kfilter.k_endog)

        # blas.daxpy(&model._k_endog2, &alpha,
        #        model._obs_cov, &inc,
        #        smoother._smoothed_measurement_disturbance_cov, &inc)
        for i in range(kfilter.k_endog):
            for j in range(i+1):
                smoother._smoothed_measurement_disturbance_cov[i + j*kfilter.k_endog] = model._obs_cov[i + j*model._k_endog] + smoother._smoothed_measurement_disturbance_cov[i + j*kfilter.k_endog]
                if not i == j:
                    smoother._smoothed_measurement_disturbance_cov[j + i*kfilter.k_endog] = model._obs_cov[j + i*model._k_endog] + smoother._smoothed_measurement_disturbance_cov[j + i*kfilter.k_endog]
        
        # Smoothed state disturbance covariance matrix  
        # $Var(\eta_t | Y_n) = Q_t - \\#_0' N_t \\#_0$  
        # $(r \times r) = (r \times r) - (r \times m) (m \times m) (m \times r)$  
        blas.dgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmp0, &kfilter.k_states,
                  &beta, smoother._tmpL, &kfilter.k_states)

        blas.dcopy(&model._k_posdef2, model._state_cov, &inc, smoother._smoothed_state_disturbance_cov, &inc)
        blas.dgemm("T", "N", &model._k_posdef, &model._k_posdef, &model._k_states,
                  &gamma, smoother._tmp0, &kfilter.k_states,
                          smoother._tmpL, &kfilter.k_states,
                  &alpha, smoother._smoothed_state_disturbance_cov, &kfilter.k_posdef)

# ### Missing Observation Conventional Kalman smoother
#
# See Durbin and Koopman (2012) Chapter 4.10
#
# Here k_endog is the same as usual, but the design matrix and observation
# covariance matrix are enforced to be zero matrices.

cdef int csmoothed_estimators_missing_conventional(cKalmanSmoother smoother, cKalmanFilter kfilter, cStatespace model) except *:
    cdef:
        int inc = 1
        np.complex64_t alpha = 1.0
        np.complex64_t beta = 0.0
        np.complex64_t gamma = -1.0

    # Scaled smoothed estimator  
    # $r_{t-1} = T_t' r_t$  
    # $(m \times 1) = (m \times m) (m \times 1)$
    # Note: save $r_{t-1}$ as scaled_smoothed_estimator[t] rather than
    # as scaled_smoothed_estimator[t-1] because we actually need to store
    # T+1 of them (r_{T-1} to r_{-1} -> r_T to r_0)
    if smoother.smoother_output & (SMOOTHER_STATE | SMOOTHER_DISTURBANCE):
        if model.identity_transition:
            blas.ccopy(&model._k_states, smoother._input_scaled_smoothed_estimator, &inc, smoother._scaled_smoothed_estimator, &inc)
        else:
            blas.cgemv("T", &model._k_states, &model._k_states,
                    &alpha, model._transition, &model._k_states,
                            smoother._input_scaled_smoothed_estimator, &inc,
                    &beta, smoother._scaled_smoothed_estimator, &inc)

    # Scaled smoothed estimator covariance matrix  
    # $N_{t-1} = T_t' N_t T_t$  
    # $(m \times m) = (m \times m) (m \times m) (m \times m)$  
    # Note: save $N_{t-1}$ as scaled_smoothed_estimator_cov[t] rather
    # than as scaled_smoothed_estimator_cov[t-1] because we actually
    # need to store T+1 of them (N_{T-1} to N_{-1} -> N_T to N_0)
    if smoother.smoother_output & (SMOOTHER_STATE_COV | SMOOTHER_DISTURBANCE_COV):
        if model.identity_transition:
            blas.ccopy(&model._k_states2, smoother._input_scaled_smoothed_estimator_cov, &inc, smoother._scaled_smoothed_estimator_cov, &inc)
        else:
            blas.cgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
                      &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                              model._transition, &model._k_states,
                      &beta, smoother._tmp0, &kfilter.k_states)
            blas.cgemm("T", "N", &kfilter.k_states, &kfilter.k_states, &kfilter.k_states,
                      &alpha, model._transition, &model._k_states,
                              smoother._tmp0, &kfilter.k_states,
                      &beta, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states)

    # $L_t = T_t$  
    blas.ccopy(&model._k_states2, model._transition, &inc, smoother._tmpL, &inc)

    # Smoothing error  
    # It is undefined here, since F_t^{-1} is nan
    # for i in range(kfilter.k_endog):
    #     smoother._smoothing_error[i] = 0

    # Smoothing error  
    # $u_t = - K_t' r_t$  
    # $(p \times 1) = (p \times 1) - (p \times m) (m \times 1)$  
    # TODO in the missing case, I think K_t is defined to be zeros, so this
    # would be unnecessary
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE):
        blas.cgemv("T", &model._k_states, &model._k_endog,
                  &gamma, kfilter._kalman_gain, &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator, &inc,
                  &beta, smoother._smoothing_error, &inc)

cdef int csmoothed_disturbances_missing_conventional(cKalmanSmoother smoother, cKalmanFilter kfilter, cStatespace model):
    cdef:
        int inc = 1
        np.complex64_t alpha = 1.0
        np.complex64_t beta = 0.0
        np.complex64_t gamma = -1.0

    # Temporary arrays

    # $\\#_0 = R_t Q_t$  
    # $(m \times r) = (m \times r) (r \times r)$
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE | SMOOTHER_DISTURBANCE_COV):
        blas.cgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_posdef,
                  &alpha, model._selection, &model._k_states,
                          model._state_cov, &model._k_posdef,
                  &beta, smoother._tmp0, &kfilter.k_states)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE:
        # Smoothed state disturbance  
        # $\hat \eta_t = \\#_0' r_t$  
        # $(r \times 1) = (r \times m) (m \times 1)$  
        blas.cgemv("T", &kfilter.k_states, &kfilter.k_posdef,
                      &alpha, smoother._tmp0, &kfilter.k_states,
                              smoother._input_scaled_smoothed_estimator, &inc,
                      &beta, smoother._smoothed_state_disturbance, &inc)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE_COV:
      # Smoothed state disturbance covariance matrix  
        # $Var(\eta_t | Y_n) = Q_t - \\#_0' N_t \\#_0$  
        # $(r \times r) = (r \times r) - (r \times m) (m \times m) (m \times r)$  
        blas.cgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmp0, &kfilter.k_states,
                  &beta, smoother._tmpL, &kfilter.k_states)
        blas.ccopy(&model._k_posdef2, model._state_cov, &inc, smoother._smoothed_state_disturbance_cov, &inc)
        blas.cgemm("T", "N", &model._k_posdef, &model._k_posdef, &model._k_states,
                  &gamma, smoother._tmp0, &kfilter.k_states,
                          smoother._tmpL, &kfilter.k_states,
                  &alpha, smoother._smoothed_state_disturbance_cov, &kfilter.k_posdef)


    # Just return the unconditional distribution for the measurement
    # disturbances corresponding to a missing observation

    # TODO this is not explicitly addressed in Durbin and Koopman Chapter 4
    # or in Koopman (1993) - need to find a source for if this is correct
    # Note: this is what the MATLAB ssm toolbox does, also

    # Smoothed measurement disturbances have unconditional expected
    # value of 0, so no need to do anything

    # Smoothed measurement and state disturbances have unconditional covariance
    # matrix of $H_t, Q_t$, respectively
    blas.ccopy(&model._k_endog2, model._obs_cov, &inc, smoother._smoothed_measurement_disturbance_cov, &inc)


# ### Conventional Kalman smoother
#
# The following are the above routines as defined in the conventional Kalman
# smoother.
#
# See Durbin and Koopman (2012) Chapter 4

cdef int csmoothed_estimators_measurement_conventional(cKalmanSmoother smoother, cKalmanFilter kfilter, cStatespace model) except *:
    cdef:
        int i
        int inc = 1
        np.complex64_t alpha = 1.0
        np.complex64_t beta = 0.0
        np.complex64_t gamma = -1.0

    # Smoothing error  
    # $u_t = \\#_2 - K_t' r_t$  
    # $(p \times 1) = (p \times 1) - (p \times m) (m \times 1)$ 
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE):
        blas.ccopy(&model._k_endog, kfilter._tmp2, &inc, smoother._smoothing_error, &inc)
        blas.cgemv("T", &model._k_states, &model._k_endog,
                  &gamma, kfilter._kalman_gain, &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator, &inc,
                  &alpha, smoother._smoothing_error, &inc)

    # $L_t = (T_t - K_t Z_t)$  = (T_t - T_t P_t Z_t' F_t^{-1} Z_t)
    # $(m \times m) = (m \times m) + (m \times p) (p \times m)$
    # (this is required for any type of smoothing)
    blas.ccopy(&model._k_states2, model._transition, &inc, smoother._tmpL, &inc)
    blas.cgemm("N", "N", &model._k_states, &model._k_states, &model._k_endog,
              &gamma, kfilter._kalman_gain, &kfilter.k_states,
                      model._design, &model._k_endog,
              &alpha, smoother._tmpL, &kfilter.k_states)

    # Scaled smoothed estimator  
    # $r_{t-1} = Z_t' \\#_2 + L_t' r_t$  
    # $(m \times 1) = (m \times p) (p \times 1) + (m \times m) (m \times 1)$
    # Note: save $r_{t-1}$ as scaled_smoothed_estimator[t] rather than
    # as scaled_smoothed_estimator[t-1] because we actually need to store
    # T+1 of them (r_{T-1} to r_{-1} -> r_T to r_0)
    if smoother.smoother_output & (SMOOTHER_STATE | SMOOTHER_DISTURBANCE):
        blas.cgemv("T", &model._k_states, &model._k_states,
                  &alpha, smoother._tmpL, &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator, &inc,
                  &beta, smoother._scaled_smoothed_estimator, &inc)

        blas.cgemv("T", &model._k_endog, &model._k_states,
                  &alpha, model._design, &model._k_endog,
                          kfilter._tmp2, &inc,
                  &alpha, smoother._scaled_smoothed_estimator, &inc)

    # Scaled smoothed estimator covariance matrix  
    # $N_{t-1} = Z_t' \\#_3 + L_t' N_t L_t$  
    # $(m \times m) = (m \times p) (p \times m) + (m \times m) (m \times m) (m \times m)$  
    # Note: save $N_{t-1}$ as scaled_smoothed_estimator_cov[t] rather
    # than as scaled_smoothed_estimator_cov[t-1] because we actually
    # need to store T+1 of them (N_{T-1} to N_{-1} -> N_T to N_0)
    if smoother.smoother_output & (SMOOTHER_STATE_COV | SMOOTHER_DISTURBANCE_COV):
        blas.cgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmpL, &kfilter.k_states,
                  &beta, smoother._tmp0, &kfilter.k_states)
        blas.cgemm("T", "N", &model._k_states, &model._k_states, &model._k_states,
                  &alpha, smoother._tmpL, &kfilter.k_states,
                          smoother._tmp0, &kfilter.k_states,
                  &beta, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states)
        blas.cgemm("T", "N", &model._k_states, &model._k_states, &model._k_endog,
                  &alpha, model._design, &model._k_endog,
                          kfilter._tmp3, &kfilter.k_endog,
                  &alpha, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states)

cdef int csmoothed_estimators_time_conventional(cKalmanSmoother smoother, cKalmanFilter kfilter, cStatespace model):
  pass

cdef int csmoothed_state_conventional(cKalmanSmoother smoother, cKalmanFilter kfilter, cStatespace model):
    cdef int i, j
    cdef:
        int inc = 1
        np.complex64_t alpha = 1.0
        np.complex64_t beta = 0.0
        np.complex64_t gamma = -1.0

    # Smoothed state
    if smoother.smoother_output & SMOOTHER_STATE:
        # $\hat \alpha_t = a_t + P_t r_{t-1}$  
        # $(m \times 1) = (m \times 1) + (m \times m) (m \times 1)$  
        blas.ccopy(&kfilter.k_states, &kfilter.predicted_state[0,smoother.t], &inc, smoother._smoothed_state, &inc)
        blas.cgemv("N", &model._k_states, &model._k_states,
                  &alpha, &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
                          smoother._scaled_smoothed_estimator, &inc,
                  &alpha, smoother._smoothed_state, &inc)

    # Smoothed state covariance
    if smoother.smoother_output & SMOOTHER_STATE_COV:
        # $V_t = P_t [I - N_{t-1} P_t]$  
        # $(m \times m) = (m \times m) [(m \times m) - (m \times m) (m \times m)]$  
        blas.cgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
              &gamma, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states,
                      &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
              &beta, smoother._tmp0, &kfilter.k_states)
        for i in range(kfilter.k_states):
            smoother.tmp0[i,i] = 1 + smoother.tmp0[i,i]
        blas.cgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
              &alpha, &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
                      smoother._tmp0, &kfilter.k_states,
              &beta, smoother._smoothed_state_cov, &kfilter.k_states)


cdef int csmoothed_state_autocov_conventional(cKalmanSmoother smoother, cKalmanFilter kfilter, cStatespace model):
    cdef:
        int i
        int inc = 1
        np.complex64_t alpha = 1.0
        np.complex64_t beta = 0.0
        np.complex64_t gamma = -1.0
    # This function computes Cov(alpha_{t+1}, alpha_t) = Cov(alpha_t, alpha_{t+1})'
    # From Durbin and Koopman, 2012, Chapter 4.7
    # Cov(alpha_{t+1}, alpha_t) = (I - P_{t+1} N_{t}) L_t P_t

    blas.cgemm("N", "N", &model.k_states, &model.k_states, &model.k_states,
                  &gamma, &kfilter.predicted_state_cov[0,0,smoother.t+1], &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                  &beta, smoother._tmp0, &kfilter.k_states)
    for i in range(kfilter.k_states):
        smoother.tmp0[i,i] = 1 + smoother.tmp0[i,i]

    blas.cgemm("N", "N", &model.k_states, &model.k_states, &model.k_states,
                  &alpha, smoother._tmpL, &kfilter.k_states,
                          &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
                  &beta, smoother._tmp_autocov, &kfilter.k_states)

    blas.cgemm("N", "N", &model.k_states, &model.k_states, &model.k_states,
                  &alpha, smoother._tmp0, &kfilter.k_states,
                          smoother._tmp_autocov, &kfilter.k_states,
                  &beta, smoother._smoothed_state_autocov, &kfilter.k_states)

cdef int csmoothed_disturbances_conventional(cKalmanSmoother smoother, cKalmanFilter kfilter, cStatespace model):
    cdef int i, j
    cdef:
        int inc = 1
        np.complex64_t alpha = 1.0
        np.complex64_t beta = 0.0
        np.complex64_t gamma = -1.0

    # Temporary arrays

    # $\\#_0 = R_t Q_t$  
    # $(m \times r) = (m \times r) (r \times r)$
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE | SMOOTHER_DISTURBANCE_COV):
        blas.cgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_posdef,
                  &alpha, model._selection, &model._k_states,
                          model._state_cov, &model._k_posdef,
                  &beta, smoother._tmp0, &kfilter.k_states)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE:
        # Smoothed measurement disturbance  
        # $\hat \varepsilon_t = H_t u_t$  
        # $(p \times 1) = (p \times p) (p \times 1)$  
        blas.cgemv("N", &model._k_endog, &model._k_endog,
                      &alpha, model._obs_cov, &model._k_endog,
                              smoother._smoothing_error, &inc,
                      &beta, smoother._smoothed_measurement_disturbance, &inc)

        # Smoothed state disturbance  
        # $\hat \eta_t = \\#_0' r_t$  
        # $(r \times 1) = (r \times m) (m \times 1)$  
        blas.cgemv("T", &model._k_states, &model._k_posdef,
                      &alpha, smoother._tmp0, &kfilter.k_states,
                              smoother._input_scaled_smoothed_estimator, &inc,
                      &beta, smoother._smoothed_state_disturbance, &inc)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE_COV:
        # $\\#_00 = K_t H_t$  
        # $(m \times p) = (m \times p) (p \times p)$  
        blas.cgemm("N", "N", &model._k_states, &model._k_endog, &model._k_endog,
                  &alpha, kfilter._kalman_gain, &kfilter.k_states,
                          model._obs_cov, &model._k_endog,
                  &beta, smoother._tmp00, &kfilter.k_states)

        # Smoothed measurement disturbance covariance matrix  
        # $Var(\varepsilon_t | Y_n) = H_t - H_t \\#_4 - \\#_00' N_t \\#_00$  
        # $(p \times p) = (p \times p) - (p \times p) (p \times p) - (p \times m) (m \times m) (m \times p)$  
        blas.cgemm("N", "N", &model._k_endog, &model._k_endog, &model._k_endog,
                  &gamma, model._obs_cov, &model._k_endog,
                          kfilter._tmp4, &kfilter.k_endog,
                  &beta, smoother._smoothed_measurement_disturbance_cov, &kfilter.k_endog)

        blas.cgemm("N", "N", &model._k_states, &model._k_endog, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmp00, &kfilter.k_states,
                  &beta, smoother._tmp000, &kfilter.k_states)

        blas.cgemm("T", "N", &model._k_endog, &model._k_endog, &model._k_states,
                  &gamma, smoother._tmp00, &kfilter.k_states,
                          smoother._tmp000, &kfilter.k_states,
                  &alpha, smoother._smoothed_measurement_disturbance_cov, &kfilter.k_endog)

        # blas.caxpy(&model._k_endog2, &alpha,
        #        model._obs_cov, &inc,
        #        smoother._smoothed_measurement_disturbance_cov, &inc)
        for i in range(kfilter.k_endog):
            for j in range(i+1):
                smoother._smoothed_measurement_disturbance_cov[i + j*kfilter.k_endog] = model._obs_cov[i + j*model._k_endog] + smoother._smoothed_measurement_disturbance_cov[i + j*kfilter.k_endog]
                if not i == j:
                    smoother._smoothed_measurement_disturbance_cov[j + i*kfilter.k_endog] = model._obs_cov[j + i*model._k_endog] + smoother._smoothed_measurement_disturbance_cov[j + i*kfilter.k_endog]
        
        # Smoothed state disturbance covariance matrix  
        # $Var(\eta_t | Y_n) = Q_t - \\#_0' N_t \\#_0$  
        # $(r \times r) = (r \times r) - (r \times m) (m \times m) (m \times r)$  
        blas.cgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmp0, &kfilter.k_states,
                  &beta, smoother._tmpL, &kfilter.k_states)

        blas.ccopy(&model._k_posdef2, model._state_cov, &inc, smoother._smoothed_state_disturbance_cov, &inc)
        blas.cgemm("T", "N", &model._k_posdef, &model._k_posdef, &model._k_states,
                  &gamma, smoother._tmp0, &kfilter.k_states,
                          smoother._tmpL, &kfilter.k_states,
                  &alpha, smoother._smoothed_state_disturbance_cov, &kfilter.k_posdef)

# ### Missing Observation Conventional Kalman smoother
#
# See Durbin and Koopman (2012) Chapter 4.10
#
# Here k_endog is the same as usual, but the design matrix and observation
# covariance matrix are enforced to be zero matrices.

cdef int zsmoothed_estimators_missing_conventional(zKalmanSmoother smoother, zKalmanFilter kfilter, zStatespace model) except *:
    cdef:
        int inc = 1
        np.complex128_t alpha = 1.0
        np.complex128_t beta = 0.0
        np.complex128_t gamma = -1.0

    # Scaled smoothed estimator  
    # $r_{t-1} = T_t' r_t$  
    # $(m \times 1) = (m \times m) (m \times 1)$
    # Note: save $r_{t-1}$ as scaled_smoothed_estimator[t] rather than
    # as scaled_smoothed_estimator[t-1] because we actually need to store
    # T+1 of them (r_{T-1} to r_{-1} -> r_T to r_0)
    if smoother.smoother_output & (SMOOTHER_STATE | SMOOTHER_DISTURBANCE):
        if model.identity_transition:
            blas.zcopy(&model._k_states, smoother._input_scaled_smoothed_estimator, &inc, smoother._scaled_smoothed_estimator, &inc)
        else:
            blas.zgemv("T", &model._k_states, &model._k_states,
                    &alpha, model._transition, &model._k_states,
                            smoother._input_scaled_smoothed_estimator, &inc,
                    &beta, smoother._scaled_smoothed_estimator, &inc)

    # Scaled smoothed estimator covariance matrix  
    # $N_{t-1} = T_t' N_t T_t$  
    # $(m \times m) = (m \times m) (m \times m) (m \times m)$  
    # Note: save $N_{t-1}$ as scaled_smoothed_estimator_cov[t] rather
    # than as scaled_smoothed_estimator_cov[t-1] because we actually
    # need to store T+1 of them (N_{T-1} to N_{-1} -> N_T to N_0)
    if smoother.smoother_output & (SMOOTHER_STATE_COV | SMOOTHER_DISTURBANCE_COV):
        if model.identity_transition:
            blas.zcopy(&model._k_states2, smoother._input_scaled_smoothed_estimator_cov, &inc, smoother._scaled_smoothed_estimator_cov, &inc)
        else:
            blas.zgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
                      &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                              model._transition, &model._k_states,
                      &beta, smoother._tmp0, &kfilter.k_states)
            blas.zgemm("T", "N", &kfilter.k_states, &kfilter.k_states, &kfilter.k_states,
                      &alpha, model._transition, &model._k_states,
                              smoother._tmp0, &kfilter.k_states,
                      &beta, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states)

    # $L_t = T_t$  
    blas.zcopy(&model._k_states2, model._transition, &inc, smoother._tmpL, &inc)

    # Smoothing error  
    # It is undefined here, since F_t^{-1} is nan
    # for i in range(kfilter.k_endog):
    #     smoother._smoothing_error[i] = 0

    # Smoothing error  
    # $u_t = - K_t' r_t$  
    # $(p \times 1) = (p \times 1) - (p \times m) (m \times 1)$  
    # TODO in the missing case, I think K_t is defined to be zeros, so this
    # would be unnecessary
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE):
        blas.zgemv("T", &model._k_states, &model._k_endog,
                  &gamma, kfilter._kalman_gain, &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator, &inc,
                  &beta, smoother._smoothing_error, &inc)

cdef int zsmoothed_disturbances_missing_conventional(zKalmanSmoother smoother, zKalmanFilter kfilter, zStatespace model):
    cdef:
        int inc = 1
        np.complex128_t alpha = 1.0
        np.complex128_t beta = 0.0
        np.complex128_t gamma = -1.0

    # Temporary arrays

    # $\\#_0 = R_t Q_t$  
    # $(m \times r) = (m \times r) (r \times r)$
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE | SMOOTHER_DISTURBANCE_COV):
        blas.zgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_posdef,
                  &alpha, model._selection, &model._k_states,
                          model._state_cov, &model._k_posdef,
                  &beta, smoother._tmp0, &kfilter.k_states)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE:
        # Smoothed state disturbance  
        # $\hat \eta_t = \\#_0' r_t$  
        # $(r \times 1) = (r \times m) (m \times 1)$  
        blas.zgemv("T", &kfilter.k_states, &kfilter.k_posdef,
                      &alpha, smoother._tmp0, &kfilter.k_states,
                              smoother._input_scaled_smoothed_estimator, &inc,
                      &beta, smoother._smoothed_state_disturbance, &inc)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE_COV:
      # Smoothed state disturbance covariance matrix  
        # $Var(\eta_t | Y_n) = Q_t - \\#_0' N_t \\#_0$  
        # $(r \times r) = (r \times r) - (r \times m) (m \times m) (m \times r)$  
        blas.zgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmp0, &kfilter.k_states,
                  &beta, smoother._tmpL, &kfilter.k_states)
        blas.zcopy(&model._k_posdef2, model._state_cov, &inc, smoother._smoothed_state_disturbance_cov, &inc)
        blas.zgemm("T", "N", &model._k_posdef, &model._k_posdef, &model._k_states,
                  &gamma, smoother._tmp0, &kfilter.k_states,
                          smoother._tmpL, &kfilter.k_states,
                  &alpha, smoother._smoothed_state_disturbance_cov, &kfilter.k_posdef)


    # Just return the unconditional distribution for the measurement
    # disturbances corresponding to a missing observation

    # TODO this is not explicitly addressed in Durbin and Koopman Chapter 4
    # or in Koopman (1993) - need to find a source for if this is correct
    # Note: this is what the MATLAB ssm toolbox does, also

    # Smoothed measurement disturbances have unconditional expected
    # value of 0, so no need to do anything

    # Smoothed measurement and state disturbances have unconditional covariance
    # matrix of $H_t, Q_t$, respectively
    blas.zcopy(&model._k_endog2, model._obs_cov, &inc, smoother._smoothed_measurement_disturbance_cov, &inc)


# ### Conventional Kalman smoother
#
# The following are the above routines as defined in the conventional Kalman
# smoother.
#
# See Durbin and Koopman (2012) Chapter 4

cdef int zsmoothed_estimators_measurement_conventional(zKalmanSmoother smoother, zKalmanFilter kfilter, zStatespace model) except *:
    cdef:
        int i
        int inc = 1
        np.complex128_t alpha = 1.0
        np.complex128_t beta = 0.0
        np.complex128_t gamma = -1.0

    # Smoothing error  
    # $u_t = \\#_2 - K_t' r_t$  
    # $(p \times 1) = (p \times 1) - (p \times m) (m \times 1)$ 
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE):
        blas.zcopy(&model._k_endog, kfilter._tmp2, &inc, smoother._smoothing_error, &inc)
        blas.zgemv("T", &model._k_states, &model._k_endog,
                  &gamma, kfilter._kalman_gain, &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator, &inc,
                  &alpha, smoother._smoothing_error, &inc)

    # $L_t = (T_t - K_t Z_t)$  = (T_t - T_t P_t Z_t' F_t^{-1} Z_t)
    # $(m \times m) = (m \times m) + (m \times p) (p \times m)$
    # (this is required for any type of smoothing)
    blas.zcopy(&model._k_states2, model._transition, &inc, smoother._tmpL, &inc)
    blas.zgemm("N", "N", &model._k_states, &model._k_states, &model._k_endog,
              &gamma, kfilter._kalman_gain, &kfilter.k_states,
                      model._design, &model._k_endog,
              &alpha, smoother._tmpL, &kfilter.k_states)

    # Scaled smoothed estimator  
    # $r_{t-1} = Z_t' \\#_2 + L_t' r_t$  
    # $(m \times 1) = (m \times p) (p \times 1) + (m \times m) (m \times 1)$
    # Note: save $r_{t-1}$ as scaled_smoothed_estimator[t] rather than
    # as scaled_smoothed_estimator[t-1] because we actually need to store
    # T+1 of them (r_{T-1} to r_{-1} -> r_T to r_0)
    if smoother.smoother_output & (SMOOTHER_STATE | SMOOTHER_DISTURBANCE):
        blas.zgemv("T", &model._k_states, &model._k_states,
                  &alpha, smoother._tmpL, &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator, &inc,
                  &beta, smoother._scaled_smoothed_estimator, &inc)

        blas.zgemv("T", &model._k_endog, &model._k_states,
                  &alpha, model._design, &model._k_endog,
                          kfilter._tmp2, &inc,
                  &alpha, smoother._scaled_smoothed_estimator, &inc)

    # Scaled smoothed estimator covariance matrix  
    # $N_{t-1} = Z_t' \\#_3 + L_t' N_t L_t$  
    # $(m \times m) = (m \times p) (p \times m) + (m \times m) (m \times m) (m \times m)$  
    # Note: save $N_{t-1}$ as scaled_smoothed_estimator_cov[t] rather
    # than as scaled_smoothed_estimator_cov[t-1] because we actually
    # need to store T+1 of them (N_{T-1} to N_{-1} -> N_T to N_0)
    if smoother.smoother_output & (SMOOTHER_STATE_COV | SMOOTHER_DISTURBANCE_COV):
        blas.zgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmpL, &kfilter.k_states,
                  &beta, smoother._tmp0, &kfilter.k_states)
        blas.zgemm("T", "N", &model._k_states, &model._k_states, &model._k_states,
                  &alpha, smoother._tmpL, &kfilter.k_states,
                          smoother._tmp0, &kfilter.k_states,
                  &beta, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states)
        blas.zgemm("T", "N", &model._k_states, &model._k_states, &model._k_endog,
                  &alpha, model._design, &model._k_endog,
                          kfilter._tmp3, &kfilter.k_endog,
                  &alpha, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states)

cdef int zsmoothed_estimators_time_conventional(zKalmanSmoother smoother, zKalmanFilter kfilter, zStatespace model):
  pass

cdef int zsmoothed_state_conventional(zKalmanSmoother smoother, zKalmanFilter kfilter, zStatespace model):
    cdef int i, j
    cdef:
        int inc = 1
        np.complex128_t alpha = 1.0
        np.complex128_t beta = 0.0
        np.complex128_t gamma = -1.0

    # Smoothed state
    if smoother.smoother_output & SMOOTHER_STATE:
        # $\hat \alpha_t = a_t + P_t r_{t-1}$  
        # $(m \times 1) = (m \times 1) + (m \times m) (m \times 1)$  
        blas.zcopy(&kfilter.k_states, &kfilter.predicted_state[0,smoother.t], &inc, smoother._smoothed_state, &inc)
        blas.zgemv("N", &model._k_states, &model._k_states,
                  &alpha, &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
                          smoother._scaled_smoothed_estimator, &inc,
                  &alpha, smoother._smoothed_state, &inc)

    # Smoothed state covariance
    if smoother.smoother_output & SMOOTHER_STATE_COV:
        # $V_t = P_t [I - N_{t-1} P_t]$  
        # $(m \times m) = (m \times m) [(m \times m) - (m \times m) (m \times m)]$  
        blas.zgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
              &gamma, smoother._scaled_smoothed_estimator_cov, &kfilter.k_states,
                      &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
              &beta, smoother._tmp0, &kfilter.k_states)
        for i in range(kfilter.k_states):
            smoother.tmp0[i,i] = 1 + smoother.tmp0[i,i]
        blas.zgemm("N", "N", &model._k_states, &model._k_states, &model._k_states,
              &alpha, &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
                      smoother._tmp0, &kfilter.k_states,
              &beta, smoother._smoothed_state_cov, &kfilter.k_states)


cdef int zsmoothed_state_autocov_conventional(zKalmanSmoother smoother, zKalmanFilter kfilter, zStatespace model):
    cdef:
        int i
        int inc = 1
        np.complex128_t alpha = 1.0
        np.complex128_t beta = 0.0
        np.complex128_t gamma = -1.0
    # This function computes Cov(alpha_{t+1}, alpha_t) = Cov(alpha_t, alpha_{t+1})'
    # From Durbin and Koopman, 2012, Chapter 4.7
    # Cov(alpha_{t+1}, alpha_t) = (I - P_{t+1} N_{t}) L_t P_t

    blas.zgemm("N", "N", &model.k_states, &model.k_states, &model.k_states,
                  &gamma, &kfilter.predicted_state_cov[0,0,smoother.t+1], &kfilter.k_states,
                          smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                  &beta, smoother._tmp0, &kfilter.k_states)
    for i in range(kfilter.k_states):
        smoother.tmp0[i,i] = 1 + smoother.tmp0[i,i]

    blas.zgemm("N", "N", &model.k_states, &model.k_states, &model.k_states,
                  &alpha, smoother._tmpL, &kfilter.k_states,
                          &kfilter.predicted_state_cov[0,0,smoother.t], &kfilter.k_states,
                  &beta, smoother._tmp_autocov, &kfilter.k_states)

    blas.zgemm("N", "N", &model.k_states, &model.k_states, &model.k_states,
                  &alpha, smoother._tmp0, &kfilter.k_states,
                          smoother._tmp_autocov, &kfilter.k_states,
                  &beta, smoother._smoothed_state_autocov, &kfilter.k_states)

cdef int zsmoothed_disturbances_conventional(zKalmanSmoother smoother, zKalmanFilter kfilter, zStatespace model):
    cdef int i, j
    cdef:
        int inc = 1
        np.complex128_t alpha = 1.0
        np.complex128_t beta = 0.0
        np.complex128_t gamma = -1.0

    # Temporary arrays

    # $\\#_0 = R_t Q_t$  
    # $(m \times r) = (m \times r) (r \times r)$
    if smoother.smoother_output & (SMOOTHER_DISTURBANCE | SMOOTHER_DISTURBANCE_COV):
        blas.zgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_posdef,
                  &alpha, model._selection, &model._k_states,
                          model._state_cov, &model._k_posdef,
                  &beta, smoother._tmp0, &kfilter.k_states)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE:
        # Smoothed measurement disturbance  
        # $\hat \varepsilon_t = H_t u_t$  
        # $(p \times 1) = (p \times p) (p \times 1)$  
        blas.zgemv("N", &model._k_endog, &model._k_endog,
                      &alpha, model._obs_cov, &model._k_endog,
                              smoother._smoothing_error, &inc,
                      &beta, smoother._smoothed_measurement_disturbance, &inc)

        # Smoothed state disturbance  
        # $\hat \eta_t = \\#_0' r_t$  
        # $(r \times 1) = (r \times m) (m \times 1)$  
        blas.zgemv("T", &model._k_states, &model._k_posdef,
                      &alpha, smoother._tmp0, &kfilter.k_states,
                              smoother._input_scaled_smoothed_estimator, &inc,
                      &beta, smoother._smoothed_state_disturbance, &inc)

    if smoother.smoother_output & SMOOTHER_DISTURBANCE_COV:
        # $\\#_00 = K_t H_t$  
        # $(m \times p) = (m \times p) (p \times p)$  
        blas.zgemm("N", "N", &model._k_states, &model._k_endog, &model._k_endog,
                  &alpha, kfilter._kalman_gain, &kfilter.k_states,
                          model._obs_cov, &model._k_endog,
                  &beta, smoother._tmp00, &kfilter.k_states)

        # Smoothed measurement disturbance covariance matrix  
        # $Var(\varepsilon_t | Y_n) = H_t - H_t \\#_4 - \\#_00' N_t \\#_00$  
        # $(p \times p) = (p \times p) - (p \times p) (p \times p) - (p \times m) (m \times m) (m \times p)$  
        blas.zgemm("N", "N", &model._k_endog, &model._k_endog, &model._k_endog,
                  &gamma, model._obs_cov, &model._k_endog,
                          kfilter._tmp4, &kfilter.k_endog,
                  &beta, smoother._smoothed_measurement_disturbance_cov, &kfilter.k_endog)

        blas.zgemm("N", "N", &model._k_states, &model._k_endog, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmp00, &kfilter.k_states,
                  &beta, smoother._tmp000, &kfilter.k_states)

        blas.zgemm("T", "N", &model._k_endog, &model._k_endog, &model._k_states,
                  &gamma, smoother._tmp00, &kfilter.k_states,
                          smoother._tmp000, &kfilter.k_states,
                  &alpha, smoother._smoothed_measurement_disturbance_cov, &kfilter.k_endog)

        # blas.zaxpy(&model._k_endog2, &alpha,
        #        model._obs_cov, &inc,
        #        smoother._smoothed_measurement_disturbance_cov, &inc)
        for i in range(kfilter.k_endog):
            for j in range(i+1):
                smoother._smoothed_measurement_disturbance_cov[i + j*kfilter.k_endog] = model._obs_cov[i + j*model._k_endog] + smoother._smoothed_measurement_disturbance_cov[i + j*kfilter.k_endog]
                if not i == j:
                    smoother._smoothed_measurement_disturbance_cov[j + i*kfilter.k_endog] = model._obs_cov[j + i*model._k_endog] + smoother._smoothed_measurement_disturbance_cov[j + i*kfilter.k_endog]
        
        # Smoothed state disturbance covariance matrix  
        # $Var(\eta_t | Y_n) = Q_t - \\#_0' N_t \\#_0$  
        # $(r \times r) = (r \times r) - (r \times m) (m \times m) (m \times r)$  
        blas.zgemm("N", "N", &model._k_states, &model._k_posdef, &model._k_states,
                  &alpha, smoother._input_scaled_smoothed_estimator_cov, &kfilter.k_states,
                          smoother._tmp0, &kfilter.k_states,
                  &beta, smoother._tmpL, &kfilter.k_states)

        blas.zcopy(&model._k_posdef2, model._state_cov, &inc, smoother._smoothed_state_disturbance_cov, &inc)
        blas.zgemm("T", "N", &model._k_posdef, &model._k_posdef, &model._k_states,
                  &gamma, smoother._tmp0, &kfilter.k_states,
                          smoother._tmpL, &kfilter.k_states,
                  &alpha, smoother._smoothed_state_disturbance_cov, &kfilter.k_posdef)
