import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
status = MPI.Status()

if rank == 0:
    data = {'size': [1, 3, 8],
            'name': ['disk1', 'disk2', 'disk3']}
else: 
    data = None

print(f'before broadcast, data on rank {rank} is: {data}')

data = comm.bcast(data, root=0)

print(f'after broadcast, data on rank {rank} is: {data}')