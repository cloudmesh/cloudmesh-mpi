from mpi4py import MPI
import numpy as np

# Communicator
comm = MPI.COMM_WORLD

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()

# Rank 0 gets a NumPy array containing values from 0 to 9
if rank == 0:
    data = np.arange(0,10,1, dtype='i')

# Rest of the processes get an empty buffer
else:
    data = np.zeros(10, dtype='i')

# Print data in each process
print("before broadcasting, data for rank %d is: "%comm.rank, data)

# Broadcast occurs
comm.Bcast(data, root=0)

# Print data in each process after broadcast
print("after broadcasting, data for rank %d is: "%comm.rank, data)
