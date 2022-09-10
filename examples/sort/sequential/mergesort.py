# merge sort
# https://www.educative.io/edpresso/merge-sort-in-python

import os
import click
import sys
import numpy as np
from cloudmesh.common.dotdict import dotdict

config = dotdict()
config.algorithm = sorted

config.user = "gregor"
config.node = "5090X"
config.debug = False
config.benchmark = True
config.filename = sys.argv[0].replace(".py", "")
config.id = 0
config.merge = "sequential"
n = config.size = 10000
config.min_array_size = 1

# take in input from user
for arg in sys.argv[1:]:
    if arg.startswith("node="):
        config.node = arg.split("=")[1]
    elif arg.startswith("user="):
        config.user = arg.split("=")[1]
    elif arg.startswith("n="):
        config.size = int(arg.split("=")[1])
    elif arg.startswith("id="):
        config.id = int(arg.split("=")[1])
    elif arg.startswith("alg="):
         config.algorithm = arg.split("=")[1]
    elif arg.startswith("min_array_size="):
        config.min_array_size = int(arg.split("=")[1])
    elif arg.startswith("merge="):
        config.merge = arg.split("=")[1]

# define fast merge
def sequential_merge_fast(left, right):
    if config.debug:
        print(f"L IS {left}")
        print(f"R IS {right}")
    # use python builtin sort
    return np.array(sorted(np.concatenate([left, right])))
    # use to replace call to sequential merge

def merge(arr, l, m, r):
    comp = 0
    n1 = m - l + 1
    n2 = r - m

    L = arr[l:m+1]
    R = arr[m+1:r]

    i = 0
    j = 0
    k = l

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        comp +=1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    
    return comp

def sort_builtin(arr, l, r):
    arr[l:r+1] = sorted(arr[l:r+1])
    return sorted(arr[l:r+1])

def insertionSort(arr, l, r):
    comp = 0
    for i in range(l+1, r):
 
        key = arr[i]
 
        j = i-1
        while j >= l:
            if key >= arr[j]:
                comp += 1
                break
            arr[j + 1] = arr[j]
            j -= 1
            comp += 1
        arr[j + 1] = key

    return comp

subsort = sorted
if config.algorithm == "builtin":
    subsort = sort_builtin
elif config.algorithm == "insertion":
    subsort = insertionSort

def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        if len(arr[l:r+1]) > config.min_array_size:            
            return mergeSort(arr, l, m)+mergeSort(arr, m+1, r)+merge(arr, l, m, r)

        else:
            return insertionSort(arr, l, r+1)
    
    return 0

arr = [1, 8, 3, 10, 14]
print(arr)
mergeSort(arr, 0, len(arr))
print(arr)