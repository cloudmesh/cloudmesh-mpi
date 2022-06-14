# run this program using mpiexec -n 4 python night.py

import numpy as np
from mpi4py import MPI
import random
import numpy as np
from generate import Generator
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.dotdict import dotdict
import math

config = dotdict()
# config.algorithm = "sequential_merge_python",
config.algorithm = "sequential_merge_fast"
config.user = "gregor"
config.host = "5090X"
config.debug = "True"

config.logfile = f"{config.user}-{config.host}.log"

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
    if config.debug:
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

if config.algorithm=="sequential_merge_python":
    sequential_merge = sequential_merge_python

elif config.algorithm=="sequential_merge_fast":
    sequential_merge = sequential_merge_fast


if __name__ == '__main__':
    unsorted_arr = np.zeros(n, dtype="int")
    sorted_arr = np.zeros(n, dtype="int")

    sub_size = int(n / size)
    local_arr = np.zeros(sub_size, dtype="int")
    local_tmp = np.zeros(sub_size, dtype="int")
    local_remain = np.zeros(2 * sub_size, dtype="int")

    if rank == 0:
        StopWatch.start(f"total-{rank}")
        unsorted_arr = np.array(Generator().generate_random(n))
        print(f"UNSORTED ARRAY: {unsorted_arr}")


    # Send subarray to each process
    comm.Scatter(unsorted_arr, local_arr, root=0)

    # print(sub_size)
    # print(f'Buffer in process {rank} contains: {sub_arr}')

    # Sort each subarray
    local_arr.sort()

    # print(f'Buffer in process {rank} before gathering: {sub_arr}')
    # Gather sorted subarrays into one
    
    height = size / 2
    print(f"Rank: {rank}")
    while height >= 1:
        if rank >= height and rank < height * 2:
            comm.Send(local_arr, rank - height, tag=0)
        elif rank < height:
            local_tmp = np.zeros(local_arr.size, dtype="int")
            local_remain = np.zeros(2 * local_arr.size, dtype="int")
            comm.Recv(local_tmp, rank + height, tag=0)

            i = 0
            j = 0
            for k in range(0, 2 * local_arr.size):
                if i >= local_arr.size:
                    local_remain[k] = local_tmp[j]
                    j += 1
                elif j >= local_arr.size:
                    local_remain[k] = local_arr[i]
                    i += 1
                elif local_arr[i] > local_tmp[j]:
                    local_remain[k] = local_tmp[j]
                    j += 1
                else:
                    local_remain[k] = local_arr[i]
                    i += 1
            
            local_arr = local_remain

            print(f"LOCAL ARRAY: {local_arr}")
            # print(f"LOCAL TEMP: {local_tmp}")
            # print(f"LOCAL REMAIN: {local_remain}")
        height = height / 2

    if rank == 0:
        StopWatch.stop(f"total-{rank}")
        print(f"SORTED ARRAY: {local_arr}")
    
StopWatch.benchmark(user=config.user)
StopWatch.benchmark(config.logfile, user=config.user)
