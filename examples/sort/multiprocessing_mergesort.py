#!/usr/bin/env python 

#inspired by https://devopslog.wordpress.com/2012/04/15/mergesort-example-using-python-multiprocessing/
#and https://gist.github.com/stephenmcd/39ded69946155930c347
import math
import multiprocessing
import random
import sys
from verify import verify
from generate import generate_random
from generate import generate_shuffle
from cloudmesh.common.StopWatch import StopWatch
#from sequential_mergesort import merge
from performance import multiprocessing_benchmark
from pprint import pprint

def sequential_merge(*args):
    l = []
    r = []
    if len(args) == 1: l,r = args[0]
    else: l,r = args
    #print("L IS ",end="")
    #print(l)
    #print("R IS ",end="")
    #print(r)
    res = []
    #i for left half, j for right half, k for arr
    i = j = k = 0 
    while i < len(l) and j < len(r):
        #each time choose between element at front of l or r
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
        #add to arr
    
    #add any unused elements
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
        return sequential_merge(l,r)
    return arr

def multiprocessing_mergesort(arr, processes):
    #processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=processes)
    size = int(math.ceil(float(len(arr)) / processes))
    #print(pool)
    #print(processes)
    arr1 = []
    for i in range(processes):
        arr1.append(arr[(size * i):(size * (i + 1))])
    arr1 = pool.map(sequential_mergesort, arr1)
    while len(arr1) > 1:
        #print("hello")
        extra = None
        if len(arr1) % 2 == 1:
            extra = arr1.pop()
        arr1 = [(arr1[i], arr1[i + 1]) for i in range(0, len(arr1), 2)]
        arr1 = pool.map(sequential_merge, arr1)
        if extra: arr1.append(extra)

    return arr1[0]
    #arr1 = pool.map()
    

#./multiprocessing_mergesort.py "[3]" "[10]" 10
#./multiprocessing_mergesort.py "[1,2,3,10]" "[10,100,200,1000,10000]" 10
if __name__ == "__main__":
    #processes = eval(sys.argv[1])
    #sizes = eval(sys.argv[2])
    #count = int(sys.argv[3])
    processes = multiprocessing.cpu_count()
    sizes = [10, 100, 1000]
    print(processes, sizes)
    for _p in range(1,processes):
        p = int(_p)
        for _n in sizes:
            n = int(_n)
            #print(n)
            #multiprocessing_benchmark(multiprocessing_mergesort, "multiprocessing_mergesort", p, n, count)
            multiprocessing_benchmark(multiprocessing_mergesort, "multiprocessing_mergesort", p, n)



    #a = generate_random(100)
    #processes = multiprocessing.cpu_count()
    #print(processes)
    #for p in range(1, processes):
        #multiprocessing_assess(multiprocessing_mergesort, "multiprocessing_mergesort", p, sizes)