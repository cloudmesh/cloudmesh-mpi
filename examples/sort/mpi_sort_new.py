# TODO: only scatters data but does not sort

import os
import sys
from threading import local
import argparse
import numpy as np
from mpi4py import MPI
from itertools import chain

from util.generate import Generator
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.dotdict import dotdict
from sequential.mergesort import mergesort
from multiprocessing_mergesort import multiprocessing_mergesort

def split_array(array, chunk_size):
    chunks = []
    for i in range(0, len(array), chunk_size):
        chunks.append(array[i:i + chunk_size])

    return chunks

# maps common sort aliases to functions
def get_sort_by_name(name):
    if name in ["mp", "mp-merge", "mp-mergesort", "multiprocessing_mergesort"]:
        return multiprocessing_mergesort
    elif name in ["sort", "sorted"]:
        return sorted
    elif name in ["seq", "seq-mergesort", "seq-merge", "sequential_merge", "sequential_mergesort"]:
        return mergesort

def mpi_sort(order, arr, p=1, c=1, subsort='sorted', merge='merge'):
    comm = MPI.COMM_SELF.Spawn(
        sys.executable,
        args=['child.py'],
        maxprocs=p
    )

    print(f"This is the parent {comm.Get_rank()}")

    n = len(arr)
    unsorted_arr = np.asarray(arr)
    sub_size = int(n / p)  # size of each subarray
    local_arr = np.zeros(sub_size, dtype="int")  # subarray for each process
    comm.Scatter(unsorted_arr, local_arr, root=0)


# Set up the MPI Communicator
comm = MPI.COMM_WORLD
size = comm.Get_size()

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()
if rank == 0:
    N = size * 3
    total_arr = Generator.generate_random(N)
    data = split_array(total_arr, int(N / size))
else:
    data = None

'''if rank == 0: # Process with rank 0 gets the data to be broadcast 
    N = 10
    total_arr = Generator.generate_random(N)
    data = total_arr

    for p in range(size):
        print(p)
else: # Other processes' data is empty
    total_arr = None
    data = None'''

# Print data in each process
print(f'before broadcast, data on rank {rank} is: {data}')

data = comm.scatter(data, root=0)
# Print data in each process after broadcast
print(f'after broadcast, data on rank {rank} is: {data}')

data = sorted(data)

print(f'after sorted, data on rank {rank} is: {data}')
