# TODO: this is not working and only used for scattering test of data over teh processors
#       however even that is not yet complete as no print or other way to confirm that
#       the arrya is scattered is done.

from mpi4py import MPI
import numpy as np

comm = MPI.Comm.Get_parent()
size = comm.Get_size()
rank = comm.Get_rank()

print(f'Hi from {comm.Get_rank()}/{comm.Get_size()}')

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


