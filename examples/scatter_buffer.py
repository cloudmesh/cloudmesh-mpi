from mpi4py import MPI
import numpy as np

# Communicator
comm = MPI.COMM_WORLD

# Number of processes in the communicator group
size = comm.Get_size()

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()

# Data to be sent
sendbuf = None

# Process with rank 0 populates sendbuf with a 2-D array,
# based on the number of processes in our communicator group
if rank == 0:
    sendbuf = np.zeros([size, 10], dtype='i')
    sendbuf.T[:,:] = range(size)
    
    # Print the content of sendbuf before scattering
    print('sendbuf in 0: ', sendbuf)

# Each process getd a buffer (initially containing just zeros) 
# to store scattered data.
recvbuf = np.zeros(10, dtype='i')

# Print the content of recvbuf in each process before scattering
print('recvbuf in  %d: '%rank, recvbuf)

# Scattering occurs
comm.Scatter(sendbuf, recvbuf, root=0)

# Print the content of sendbuf in each process after scattering
print('Buffer in process %d contains: '%rank, recvbuf)
