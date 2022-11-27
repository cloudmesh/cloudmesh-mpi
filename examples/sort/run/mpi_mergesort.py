# run this program using mpiexec -n 4 python mpi_mergesort.py

# http://selkie-macalester.org/csinparallel/modules/MPIProgramming/build/html/mergeSort/mergeSort.html#parallel-algorithm

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
n = 2 ** 10


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
    if config.debug:
        print(f"L IS {l}")
        print(f"R IS {r}")
    return sorted(l + r)
    # use to replace call to sequential merge


if config.algorithm == "sequential_merge_python":
    sequential_merge = sequential_merge_python

elif config.algorithm == "sequential_merge_fast":
    sequential_merge = sequential_merge_fast


def mpi_mergesort(height, id, local_arr, size, comm, global_arr):
    cur_height = 0
    local_arr = sorted(local_arr)

    half1 = np.array(local_arr, dtype=int)
    # half2 = np.zeros(size, dtype="int")
    # res = np.zeros(size * 2, dtype="int")

    while cur_height < height:
        parent = (id & (~(1 << cur_height)))  # switch with |

        if parent == id:
            right_child = (id | (1 << cur_height))

            half2 = np.zeros(size, dtype="int")
            comm.Recv([half2, MPI.INT], source=right_child)  # may need to change
            if config.debug:
                print(f"HALF2 {half2}")
            res = np.zeros(size * 2, dtype="int")
            res = sequential_merge(half1, half2)

            half1 = res
            size *= 2
            # do i have to free half2
            res = None

            cur_height += 1

        else:
            print("HERE AT 72")
            half1 = np.array(local_arr, dtype=int)

            comm.Send([half1, MPI.INT], dest=parent)
            if cur_height != 0:
                half1 = None
                del half1
            cur_height = height

    if id == 0:
        global_arr = half1

    return global_arr


if __name__ == '__main__':
    num_procs = size
    id = rank
    height = math.log2(num_procs)

    global_arr = np.zeros(n, dtype="int")

    if rank == 0:
        StopWatch.start(f"total-{rank}")
        global_arr = np.array(Generator().generate_random(n))
        print(f"UNSORTED ARRAY: {global_arr}")

    sub_size = int(n / num_procs)
    local_arr = np.zeros(sub_size, dtype="int")

    comm.Scatter(global_arr, local_arr, root=0)

    if id == 0:
        global_arr = mpi_mergesort(height, id, local_arr, sub_size, comm, global_arr)

    else:
        mpi_mergesort(height, id, local_arr, sub_size, comm, None)

    if id == 0:
        StopWatch.stop(f"total-{rank}")
        print(f"SORTED ARRAY: {global_arr}")

    StopWatch.benchmark(user=config.user, host=config.host)
    StopWatch.benchmark(config.logfile, user=config.user, host=config.host)
