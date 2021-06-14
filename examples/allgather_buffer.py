
from mpi4py import MPI
import numpy as np



# Communicator group
comm = MPI.COMM_WORLD

# Number of processes in the communicator group 
size = comm.Get_size()

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()

# Initialize array and table
row  = np.zeros(size)
table = np.zeros((size, size))

# Each process computes the local values and fills its array
for i in range(size):
    j = i * rank
    row[i] = j

# Print array in each process
print("Process %d table before Allgather: "%rank, table, "\n")

# Gathering occurs
comm.Allgather([row,  MPI.INT], [table, MPI.INT])

# Print table in each process after gathering
print("Process %d table after Allgather: "%rank, table, "\n")
