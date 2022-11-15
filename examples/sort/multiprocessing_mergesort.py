# inspired by https://devopslog.wordpress.com/2012/04/15/mergesort-example-using-python-multiprocessing/
# and https://gist.github.com/stephenmcd/39ded69946155930c347
import math
import multiprocessing
import numpy as np

def sequential_merge(*args):
    l = []
    r = []
    if len(args) == 1:
        l, r = args[0]
    else:
        l, r = args
    res = []
    i = j = k = 0
    while i < len(l) and j < len(r):
        # each time choose between element at front of l or r
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    # add any unused elements
    while i < len(l):
        res.append(l[i])
        i += 1
    while j < len(r):
        res.append(r[j])
        j += 1
    return res


def sequential_mergesort(arr):
    n = len(arr)
    if n > 1:
        mid = int(n / 2)
        l = sequential_mergesort(arr[:mid])
        r = sequential_mergesort(arr[mid:])
        return sequential_merge(l, r)
    return arr

def fast_sort(arr):
    ans = sorted(arr)
    return ans

def multiprocessing_mergesort(arr, processes):
    pool = multiprocessing.Pool(processes=processes)
    size = int(math.ceil(float(len(arr)) / processes))
    arr1 = []
    for i in range(processes):
        arr1.append(arr[(size * i):(size * (i + 1))])
    arr1 = pool.map(fast_sort, arr1)
    while len(arr1) > 1:
        extra = None
        if len(arr1) % 2 == 1:
            extra = arr1.pop()
        arr1 = [(arr1[i], arr1[i + 1]) for i in range(0, len(arr1), 2)]
        arr1 = pool.map(sequential_merge, arr1)
        if extra: arr1.append(extra)

    return arr1[0]
