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
from generate import Generator
from sequential.mergesort import merge_sort
from multiprocessing_mergesort import multiprocessing_mergesort

config = dotdict()

config.user = "alex"
config.node = "v100"
config.debug = False
n = config.size = 10000
config.subsort = "sorted"
config.sort = "mpi"
config.c = 1
config.p = 1

# take in input from user
for arg in sys.argv[1:]:
    if arg.startswith("n="):
        config.size = int(arg.split("=")[1])
    if arg.startswith("user="):
        config.user = arg.split("=")[1]
    if arg.startswith("node="):
        config.node = arg.split("=")[1]
    if arg.startswith("subsort="):
        config.subsort = arg.split("=")[1]
    if arg.startswith("c="):
        config.c = int(arg.split("=")[1])
    if arg.startswith("p="):
        config.p = int(arg.split("=")[1])

# define fast merge
def fast_merge(left, right):
    if config.debug:
        print(f"L IS {left}")
        print(f"R IS {right}")
    # use python builtin sort
    return sorted(left + right)
    # use to replace call to sequential merge

def _sorted(arr, c):
    return sorted(arr)

def get_sort_by_name(name):
    if name in ["mp", "mp-merge", "mp-mergesort", "multiprocessing_mergesort"]:
        # print("MP SORT")
        return multiprocessing_mergesort
    elif name in ["sort", "sorted"]:
        # print("MERGE SORT")
        return _sorted
    elif name in ["seq", "seq-mergesort", "seq-merge", "sequential_merge", "sequential_mergesort"]:
        # print("MERGE SORT")
        return merge_sort

# check if array is sorted
def is_sorted(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1))

sort_algorithm = get_sort_by_name(config.subsort)
# tmp_unsorted_arr = np.array(Generator().generate_random(n))

StopWatch.start("mpi-mergesort")
# initialize MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
status = MPI.Status()

n = config.size

# create necessary arrays
unsorted_arr = np.zeros(n, dtype="int")
sorted_arr = np.zeros(n, dtype="int")
sub_size = int(n / size) # size of each subarray
local_arr = np.zeros(sub_size, dtype="int") # array for each process
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
    StopWatch.stop("mpi-mergesort")
    StopWatch.benchmark(tag=str(config))
    if config.debug:
        print("SIZE OF ARRAY:", config.size)
        print("IS SORTED:", is_sorted(local_arr))
        print(f"SORTED ARRAY: {local_arr}")

