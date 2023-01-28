#!/usr/bin/env python
from mpi4py import MPI

# Set up the MPI Communicator
comm = MPI.COMM_WORLD

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()

if rank == 0: # Process with rank 0 gets the data to be broadcast
    data = {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}

else: # Other processes' data is empty
    data = None

print(f'before broadcast, data on rank {rank} is: {data}')

data = comm.bcast(data, root=0)

print(f'after broadcast, data on rank {rank} is: {data}')