import os
import sys
from threading import local
import argparse
import numpy as np
from mpi4py import MPI
from itertools import chain

from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.dotdict import dotdict
#from util.generate import Generator
from sequential.mergesort import mergesort
from multiprocessing_mergesort import multiprocessing_mergesort

def get_sort_by_name(name):
    if name in ["mp", "mp-merge", "mp-mergesort", "multiprocessing_mergesort"]:
        return multiprocessing_mergesort
    elif name in ["sort", "sorted"]:
        return sorted
    elif name in ["seq", "seq-mergesort", "seq-merge", "sequential_merge", "sequential_mergesort"]:
        return mergesort\


sort_algorithm = get_sort_by_name(subsort)
    merge_algorithm = mergesort

    # initialize MPI
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    n = len(arr)

    # create necessary arrays
    unsorted_arr = np.asarray(arr)
    sorted_arr = np.zeros(n, dtype="int")

    sub_size = int(n / size)  # size of each subarray
    local_arr = np.zeros(sub_size, dtype="int")  # subarray for each process
    local_tmp = np.zeros(sub_size, dtype="int")
    local_result = np.zeros(2 * sub_size, dtype="int")

    # send subarray to each process
    comm.Scatter(unsorted_arr, local_arr, root=0)

    # print(f'Buffer in process {rank} contains: {local_arr}, size = {len(local_arr)}')

if __name__ == '__main__':
    mpi_sort()

            # print(f"SORT ALGORITHM BEING USED: {sort_algorithm}")
    # print(f"NUMBER OF CORES BEING USED: {config.c}")
    if sort_algorithm == multiprocessing_mergesort:
        local_arr = multiprocessing_mergesort(order, local_arr, c)
    elif sort_algorithm == sorted:
        local_arr = np.asarray(sorted(local_arr))
    else: 
        local_arr = sort_algorithm(order, local_arr)

    # print(f'Buffer in process {rank} before gathering: {local_arr}')
    # Gather sorted subarrays into one
    comm.Barrier()

    split = size / 2
    # print(f"Rank: {rank}")
    while split >= 1:
        if split <= rank < split * 2:
            comm.Send(local_arr, rank - split, tag=0)
        elif rank < split:
            local_tmp = np.zeros(local_arr.size, dtype="int")
            local_result = np.zeros(2 * local_arr.size, dtype="int")
            comm.Recv(local_tmp, rank + split, tag=0)

            local_result = merge_algorithm('<', local_arr + local_tmp)
            local_arr = np.array(local_result)
        split = split / 2

    # comm.Barrier()
    # comm.Gather(local_arr, sorted_arr, root=0)

    if rank == 0:
        return local_arr
