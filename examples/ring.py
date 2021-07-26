#!/usr/bin/env python
from mpi4py import MPI

# Communicator
comm = MPI.COMM_WORLD

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()
# Get the size of the communicator group
size = comm.Get_size()

if rank == 0:
    print(f'Communicator group with {size} processes')
    # User provides data to transmit through the ring
    data = int(input('Enter an integer to transmit: '))
    # Data is modified
    data += 1
    # Data is sent to next process in the ring
    comm.send(data, dest=rank + 1)
    print(f'Process {0} transmitted value {data} to process {rank + 1}')
    # Data is received from last process in the ring
    data = comm.recv(data, source=size - 1)
    print(f'Final data received in process 0 after ring is completed: {data}')

if rank == size - 1:
    # Data is received from previous process in the ring
    data = comm.recv(source=rank - 1)
    # Data is modified
    data += 1
    # Data is sent to process 0, closing the ring
    comm.send(data, dest=0)
    print(f'Process {rank} transmitted value {data} to process 0')

elif 0 < rank < size -1:
    # Data is received from previous process in the ring
    data = comm.recv(source=rank - 1)
    # Data is modified
    data += 1
    # Data is sent to next process in the ring
    comm.send(data, dest=rank + 1)
    print(f'Process {rank} transmitted value {data} to process {rank + 1}')
