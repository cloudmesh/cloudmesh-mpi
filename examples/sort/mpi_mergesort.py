import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
status = MPI.Status()

N = 16
unsorted = np.zeros(N, dtype="int")
final_sorted = np.zeros(N, dtype="int")
local_array = np.zeros(int(N / size), dtype="int")
local_tmp = np.zeros(int(N / size), dtype="int")
local_remain = np.zeros(2 * int(N / size), dtype="int")