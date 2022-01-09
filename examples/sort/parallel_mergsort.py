import math
import multiprocessing
import random
import sys
from verify import verify
from generate import generate_random
from generate import generate_shuffle
from cloudmesh.common.StopWatch import StopWatch
from performance import assess

def merge(l, r):
    arr = []
    i = j = 0 
    while i < len(l) and j < len(r):
        #each time choose between element at front of l or r
        if l[i] <= r[j]:
            arr.append(l[i])
            i += 1
        else:
            arr.append(r[j])
            j += 1
    
    #add any unused elements
    while i < len(l):
        arr.append(l[i])
        i += 1
    while j < len(r):
        arr.append(r[j])
        j += 1
    return arr 

def sort(arr):
    n = len(arr)
    if n <= 1: return arr
    mid = int(n / 2)
    l = sort(arr[:mid])
    r = sort(arr[mid:])
    return merge(l, r)

def parallel_merge_sort(arr):
    processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=processes)
    size = int(math.ceil(float(len(arr)) / processes))
    print(pool)
    print(processes)
    arr1 = []
    for i in range(processes):
        arr1.append(arr[(size * i):(size * (i + 1))])
    arr1 = pool.map()
    

if __name__ == "__main__":
    a = generate_random(100)
    print(a)
    parallel_merge_sort(a)
    print(a)