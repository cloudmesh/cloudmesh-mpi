import os
import sys
from threading import local
import argparse
import numpy as np
import multiprocessing
from mpi4py import MPI
from itertools import chain

from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.dotdict import dotdict
#from util.generate import Generator
from sequential.mergesort import merge_sort
from multiprocessing.multiprocessing_mergesort import multiprocessing_mergesort

config = dotdict()

def mpi_sort(order, arr, p=1, c=1, subsort='sorted', sort=merge_sort):

    sort_algorithm = get_sort_by_name(config.subsort)
    # tmp_unsorted_arr = np.array(Generator().generate_random(n))

    # initialize MPI
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    status = MPI.Status()

    n = config.size

    # create necessary arrays
    unsorted_arr = np.zeros(n, dtype="int")
    sorted_arr = np.zeros(n, dtype="int")
    sub_size = int(n / size)  # size of each subarray
    local_arr = np.zeros(sub_size, dtype="int")  # array for each process
    local_tmp = np.zeros(sub_size, dtype="int")
    local_result = np.zeros(2 * sub_size, dtype="int")

    # generate unsorted array on rank 0
    if rank == 0:
        StopWatch.start("mpi-generate")
        unsorted_arr = np.random.randint(n, size=n)
        StopWatch.stop("mpi-generate")
        if config.debug:
            print(f"UNSORTED ARRAY: {unsorted_arr}")

    # send subarray to each process
    comm.Scatter(unsorted_arr, local_arr, root=0)

    if config.debug:
        print(f'Buffer in process {rank} contains: {local_arr}, size = {len(local_arr)}')

    # sort each subarray
    # local_arr.sort()
    # print(f"THIS IS THE SORT ALGORITHM BEING USED: {sort_algorithm}")
    # print(f"THIS IS THE NUMNER OF CORES BEING USED: {config.c}")
    local_arr = np.array(sort_algorithm(list(local_arr), config.c))

    if config.debug:
        print(f'Buffer in process {rank} before gathering: {local_arr}')
    # Gather sorted subarrays into one

    # data = comm.gather(local_arr,root=0)

    comm.Barrier()

    split = size / 2
    if config.debug:
        print(f"Rank: {rank}")
    while split >= 1:
        if split <= rank < split * 2:
            comm.Send(local_arr, rank - split, tag=0)
        elif rank < split:
            local_tmp = np.zeros(local_arr.size, dtype="int")
            local_result = np.zeros(2 * local_arr.size, dtype="int")
            comm.Recv(local_tmp, rank + split, tag=0)

            local_result = fast_merge(local_arr, local_tmp)

            local_arr = np.array(local_result)
        split = split / 2

    # comm.Barrier()
    # comm.Gather(local_arr, sorted_arr, root=0)

    if rank == 0:
        # ans = sorted(sorted_arr)
        StopWatch.benchmark(tag=str(config))
        if config.debug:
            print("SIZE OF ARRAY:", config.size)
            print("IS SORTED:", is_sorted(local_arr))
            print(f"SORTED ARRAY: {local_arr}")
