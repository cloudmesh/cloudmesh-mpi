# TODO: this does not work, as only data is scattered, but the mpi
#       method does not actutlly call sort.

import os
import sys
from threading import local
import argparse
import numpy as np
from mpi4py import MPI
from itertools import chain

from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.dotdict import dotdict
from sequential.mergesort import mergesort
from multiprocessing_mergesort import multiprocessing_mergesort

data = dotdict()
for arg in sys.argv[1]:
    if arg.

config = dotdict()
config.algorithm = "sequential_merge_fast"

config.user = "alex"
config.node = "v100"
config.debug = False
n = config.size = 10000
config.sort = "sorted"
config.c = 1

# take in input from user
for arg in sys.argv[1:]:
    if arg.startswith("n="):
        config.size = int(arg.split("=")[1])
    if arg.startswith("user="):
        config.user = arg.split("=")[1]
    if arg.startswith("node="):
        config.node = arg.split("=")[1]
    if arg.startswith("sort="):
        config.sort = arg.split("=")[1]
    if arg.startswith("c="):
        config.c = int(arg.split("=")[1])


# maps common sort aliases to functions
def get_sort_by_name(name):
    if name in ["mp", "mp-merge", "mp-mergesort", "multiprocessing_mergesort"]:
        return multiprocessing_mergesort
    elif name in ["sort", "sorted"]:
        return sorted
    elif name in ["seq", "seq-mergesort", "seq-merge", "sequential_merge", "sequential_mergesort"]:
        return mergesort

def mpi_sort(order,
             arr,
             p=1,
             c=1,
             subsort='sorted',
             merge='merge'):
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