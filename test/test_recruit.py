import time

from .task_fib import fib
import recruit


def profile_worker(worker, job_argument):
    start = time.time()
    result = worker.send(job_argument)
    elapsed = time.time() - start

    start2 = time.time()
    result_str = repr(result)
    elapsed2 = time.time() - start2

    print(f'{worker} takes job in {elapsed} s, and finishes job with result {result_str} in {elapsed2} s')


job_argument = 30
profile_worker(recruit.Self(fib), job_argument)
profile_worker(recruit.Contractor(fib), job_argument)
profile_worker(recruit.FullTimeEmployee(fib), job_argument)
