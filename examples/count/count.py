# Run with
#     mpiexec -n 4 python count.py

# To change the values set them on your terminal on the
# machine running rank 0 with 

# export N=20
# export MAX=10
# export FIND=8

# Assignment:
# Add to this code the bradcast of the 3 parameters to all workers

import os
import random
from mpi4py import MPI

# Get the input values or set them to a default
n = int(os.environ.get("N") or 20)
max_number = int(os.environ.get("MAX") or 10)
find = int(os.environ.get("FIND") or 8)


comm = MPI.COMM_WORLD   # Communicator
size = comm.Get_size()  # Number of processes 
rank = comm.Get_rank()  # Rank of this process

# Each process gets different data, depending on its rank number
data = []
for i in range(n):
    r = random.randint(1, max_number)
    data.append(r)
count = data.count(find)

print(rank, count, data)  # Print data from each process
count_data = comm.gather(count, root=0) # Gather the data

# Process 0 prints out the gathered data, rest of the processes
if rank == 0:
    print(rank, count_data)
    total = sum(count_data)
    print(f"Total number of {find}'s:", total)

