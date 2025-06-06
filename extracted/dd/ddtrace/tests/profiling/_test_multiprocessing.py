import multiprocessing
import os
import sys
import time


def f():
    import ddtrace.profiling.bootstrap

    profiler = ddtrace.profiling.bootstrap.profiler
    for _ in range(50):
        time.sleep(0.1)
    # Manually stop the profiler: atexit hooks are not called in subprocesses launched by multiprocessing and we want to
    # be sure the profile are flushed out
    profiler.stop()


if __name__ == "__main__":
    print(os.getpid())
    multiprocessing.set_start_method(sys.argv[1], force=True)

    p = multiprocessing.Process(target=f)
    p.start()
    print(p.pid)
    p.join(120)
