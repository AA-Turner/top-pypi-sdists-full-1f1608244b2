#ifndef DAQP_UTILS_H
# define DAQP_UTILS_H

# ifdef __cplusplus
extern "C" {
# endif // ifdef __cplusplus

#include "daqp.h"
// Utils for transforming QP to LDP
int update_ldp(const int mask, DAQPWorkspace *work, DAQPProblem *qp);
int update_Rinv(DAQPWorkspace *work, c_float *H);
void update_M(DAQPWorkspace *work, c_float *A, const int mask);
void update_v(c_float *f, DAQPWorkspace *work, const int mask);
int update_d(DAQPWorkspace *work, c_float *bupper, c_float *blower);
void normalize_Rinv(DAQPWorkspace *work);
void normalize_M(DAQPWorkspace *work);
//
void daqp_minrep_work(int* is_redundant,DAQPWorkspace* work);
// Utils for profiling
#ifdef PROFILING
#ifdef _WIN32
#include <windows.h>
typedef struct{ 
    LARGE_INTEGER start;
    LARGE_INTEGER stop;
}DAQPtimer;
#else // not _WIN32 
#include <time.h>
typedef struct{ 
    struct timespec start;
    struct timespec stop;
}DAQPtimer;
#endif // _WIN32


void tic(DAQPtimer *timer);
void toc(DAQPtimer *timer);
double get_time(DAQPtimer *timer);
#endif // PROFILING

# ifdef __cplusplus
}
# endif // ifdef __cplusplus

#endif //ifndef DAQP_UTILS_H
