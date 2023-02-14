# inspired by https://devopslog.wordpress.com/2012/04/15/mergesort-example-using-python-multiprocessing/
# and https://gist.github.com/stephenmcd/39ded69946155930c347
import math
import multiprocessing
import numpy as np
from itertools import chain
# from .sequential.mergesort import mergesort as sequential_mergsort_best


def fast_sort(arr):
    ans = sorted(arr)
    return ans

def multiprocessing_mergesort(order, arr, processes):
    # print(f"PROCESSES: {processes}")
    pool = multiprocessing.Pool(processes=processes)
    size = int(math.ceil(float(len(arr)) / processes))
    arr1 = []
    for i in range(processes):
        arr1.append(arr[(size * i):(size * (i + 1))])
    arr1 = pool.map(fast_sort, arr1)
    pool.close()
    ans = sorted(list(chain.from_iterable(arr1)))
    return np.array(ans)
