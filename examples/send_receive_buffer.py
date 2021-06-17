#!/usr/bin/env python
import numpy as np
from mpi4py import MPI


# Communicator
comm = MPI.COMM_WORLD

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()

# Create empty buffer to receive data
buf = np.zeros(5, dtype=int)

# Process with rank 0 sends data to process with rank 1
if rank == 0:
   data = np.arange(1, 6)
   comm.Send([data, MPI.INT], dest=1)


# Process with rank 1 receives and stores data
if rank == 1:
   comm.Recv([buf, MPI.INT], source=0)

# Each process in the communicator group prints the content of its buffer
print(f'After send/receive, the value in process {rank} is {buf}')
