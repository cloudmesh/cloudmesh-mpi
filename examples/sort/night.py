# run this program using mpiexec -n 4 python mpi_mergesort.py

# http://selkie-macalester.org/csinparallel/modules/MPIProgramming/build/html/mergeSort/mergeSort.html#parallel-algorithm

import numpy as np
from mpi4py import MPI
import random
import numpy as np
from generate import Generator
from cloudmesh.common.StopWatch import StopWatch
import math

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
status = MPI.Status()
n = 2 ** 8

def sequential_merge_python(a, b, l, m, r):
    h = l
    i = l
    j = m + 1

    while h <= m and j <= r:
        if a[h] <= a[j]: 
            b[i] = a[h]
            h += 1
            
        else:
            b[i] = a[j]
            j += 1
            
        i += 1
        
    if m < h:
        for k in range(j, r + 1):
            b[i] = a[k]
            i += 1
            
    else:
        for k in range(h, m + 1):
            b[i] = a[k]
            i += 1
            
    for k in range(l, r + 1):
        a[k] = b[k]

def sequential_merge_fast(l, r):
    print(f"L IS {l}")
    print(f"R IS {r}")
    return sorted(l + r)
    # use to replace call to sequential merge
    
sequential_merge = sequential_merge_fast

def merge_sort(a, b, l, r):
    if l < r:
        m = int((l + r) / 2)

        merge_sort(a, b, l, m)
        merge_sort(a, b, m + 1, r)
        sequential_merge(a, b, l, m, r)


if __name__ == '__main__':
    global_arr = np.zeros(n, dtype="int")
    sub_size = int(n / size)

    if rank == 0:
        global_arr = np.array(Generator().generate_random(n))
        print(f"UNSORTED ARRAY: {global_arr}")

        global_arr = np.reshape(global_arr, (-1, sub_size))
        # print(global_arr)


    # Send subarray to each process
    sub_arr = np.zeros(sub_size, dtype="int")
    comm.Scatter(global_arr, sub_arr, root=0)

    # print(sub_size)
    print(f'Buffer in process {rank} contains: {sub_arr}')

    # Sort each subarray
    sub_arr = sorted(sub_arr)

    print(f'Buffer in process {rank} before gathering: {sub_arr}')
    # Gather sorted subarrays into one
    sorted = None
    if rank == 0:
        sorted = np.zeros([size, sub_size], dtype="int")
        print(f'recvbuf in process 0 before gathering: {sorted}')
     
     
    comm.Gather(sub_arr, sorted, root=0)
    if rank == 0:
        print(f'recvbuf in process 0 after gathering: \n{sorted}')
    

