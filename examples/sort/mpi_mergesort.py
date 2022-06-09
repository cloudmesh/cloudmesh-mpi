# http://selkie-macalester.org/csinparallel/modules/MPIProgramming/build/html/mergeSort/mergeSort.html#parallel-algorithm

from asyncio.windows_events import NULL
import numpy as np
from mpi4py import MPI
from mpi4py import MPI
import random
import numpy as np
from generate import Generator
from cloudmesh.common.StopWatch import StopWatch
import math

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank
status = MPI.Status()

def sequential_merge_python(l, r):
    size_1 = len(l) 
    size_2 = len(r) 
  
    res = [] 
    i, j = 0, 0
  
    while i < size_1 and j < size_2: 
        if l[i] < r[j]:   
          res.append(l[i]) 
          i += 1
  
        else: 
          res.append(r[j]) 
          j += 1
  
    res = res + l[i:] + r[j:]
    return res

def sequential_merge_fast(l, r):
    return sorted(l + r)
    # use to replace call to sequential merge
    
sequential_merge = sequential_merge_fast

def mpi_mergesort(height, id, local_arr, size, comm, global_arr):
    cur_height = 0
    local_arr = sorted(local_arr)

    half1 = local_arr
    half2 = []
    res = []

    while cur_height < height:
        parent = (id & (~(1 << cur_height))) # switch with |

        if parent == id:
            right_child = (id | (1 << cur_height))

            half2 = comm.recv(source=right_child) # may need to change

            res = sequential_merge(half1, half2)

            half1 = res

            size *= 2

            res = NULL

            cur_height += 1
        
        else:
            comm.send(half1, dest=parent)
            if cur_height != 0:
                half2 = []
            cur_height = height

    if id == 0:
        global_arr = half1
    
    return global_arr

if __name__ == '__main__':
    global_arr = []
    num_procs = size
    id = rank

    n = 2 ** 20
    height = math.log2(num_procs, 2)

    if id == 0:
        global_arr = a = Generator().generate_random(n)
    
    sub_size = int(n / num_procs)
    comm.scatter(global_arr, root=0)

    if id == 0:
        global_arr = mpi_mergesort(height, id, loca)