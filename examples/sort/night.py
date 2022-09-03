###########################################################
# run this program using mpiexec -n 4 python night.py user=gregor node=5950X n=100
###########################################################
import os
import sys
from threading import local

import numpy as np
from mpi4py import MPI

from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.dotdict import dotdict
from sequential.mergesort import mergesort
from generate import Generator
from generate import Generator
from pprint import pprint
from adaptive_merge import adaptive_merge

config = dotdict()
config.algorithm = "sequential_merge_fast"

config.user = "gregor"
config.node = "5090X"
config.debug = False
config.benchmark = True
config.filename = sys.argv[0].replace(".py", "")
config.id = 0
n = config.size = 10000

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

# generate label for stopwatches
label = f"{config.user}-{config.node}-{config.filename}-{config.id}"
config.logfile = f"{label}.log"

# define sequential merge
def sequential_merge_python(local_arr, local_tmp):
    n = local_arr.size + local_tmp.size
    res = np.zeros(n)
    i = 0
    j = 0
    for k in range(0, local_arr.size):
        # one array is done, take all values from the other array
        if i >= local_arr.size:
            res[k] = local_tmp[j]
            j += 1
        elif j >= local_arr.size:
            res[k] = local_arr[i]
            i += 1
        # take the smaller value from the front of the arrays
        elif local_arr[i] > local_tmp[j]:
            res[k] = local_tmp[j]
            j += 1
        else:
            res[k] = local_arr[i]
            i += 1
    return res

# define fast merge
def sequential_merge_fast(left, right):
    if config.debug:
        print(f"L IS {left}")
        print(f"R IS {right}")
    # use python builtin sort
    return sorted(left + right)
    # use to replace call to sequential merge

# set merge algorithm based on user input
merge = sequential_merge_fast
if config.algorithm == "sequential_merge_python":
    merge = sequential_merge_python
elif config.algorithm == "sequential_merge_fast":
    merge = sequential_merge_fast
elif config.algorithm == "adaptive_merge":
    merge = adaptive_merge
elif config.algorithm == "timsort":
    merge = timSort

# check if array is sorted
def is_sorted(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1))


# initialize MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
status = MPI.Status()

<<<<<<< HEAD
if config.benchmark and rank == 0:
    pprint(config)

    StopWatch.start(f"{label}-total")


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


def sequential_merge_fast(left, right):
    if config.debug:
        print(f"L IS {left}")
        print(f"R IS {right}")
    return sorted(left + right)
    # use to replace call to sequential merge


sequential_merge = sequential_merge_fast

if config.algorithm == "sequential_merge_python":
    sequential_merge = sequential_merge_python

elif config.algorithm == "sequential_merge_fast":
    sequential_merge = sequential_merge_fast


=======
>>>>>>> 800dc5134ccc06e60e54befe8a4ee2f8ec77e068
n = config.size

# create necessary arrays
unsorted_arr = np.zeros(n, dtype="int")
sorted_arr = np.zeros(n, dtype="int")

sub_size = int(n / size) # size of each subarray
local_arr = np.zeros(sub_size, dtype="int") # array for each process
local_tmp = np.zeros(sub_size, dtype="int")
local_result = np.zeros(2 * sub_size, dtype="int")

# begin stopwatch for each rank
StopWatch.start(f"{rank}-time")

# generate unsorted array on rank 0
if rank == 0:
    unsorted_arr = np.array(Generator().generate_random(n))
    if config.debug:
        print(f"UNSORTED ARRAY: {unsorted_arr}")

# send subarray to each process
comm.Scatter(unsorted_arr, local_arr, root=0)

if config.debug:
    print(f'Buffer in process {rank} contains: {local_arr}, size = {len(local_arr)}')

# sort each subarray
# local_arr.sort()
local_arr = np.array(sorted(local_arr))

# print(f'Buffer in process {rank} before gathering: {sub_arr}')
# Gather sorted subarrays into one

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

        local_result = merge(local_arr, local_tmp)

        local_arr = np.array(local_result)

        if config.debug:
            # print(f"LOCAL ARRAY: {local_arr}")
            # print(f"LOCAL TEMP: {local_tmp}")
            print(f"LOCAL REMAIN: {local_result}")
    split = split / 2

StopWatch.stop(f"{rank}-time")
info = StopWatch.__str__()
# print(info)

all_info = comm.gather(info, root=0)

# get finish msg form each worker on rank 0 and only then continue


if config.benchamrk and rank == 0:
    StopWatch.stop(f"{label}-total")
    total_time = StopWatch.__str__()
    if config.debug:
        print(f"TOTAL: {total_time}")
    # StopWatch.benchmark(user=config.user, node=config.node, sysinfo=False)

    if config.debug:
        for s in all_info:
            print(s)
        print("SIZE OF ARRAY:", config.size)
        print("IS SORTED:", is_sorted(local_arr))
        print(f"SORTED ARRAY: {local_arr}")

<<<<<<< HEAD
    print("SIZE OF ARRAY:", config.n)
    print("IS SORTED:", is_sorted(local_arr))

# MPI.Finalize()
=======
>>>>>>> 800dc5134ccc06e60e54befe8a4ee2f8ec77e068
