import random
from mpi4py import MPI

# Communicator
comm = MPI.COMM_WORLD

N = 20
max_number = 10
find = 8

# Number of processes in the communicator group
size = comm.Get_size()

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()

# Each process gets different data, depending on its rank number
data = []
for i in range(N):
    r = random.randint(1,max_number)
    data.append(r)
count = data.count(find)

# Print data in each process
print(rank,count,data)

# Gathering occurs
count_data = comm.gather(count, root=0)

# Process 0 prints out the gathered data, rest of the processes
# print their data as well
if rank == 0:
    print(rank, count_data)
    b = sum(count_data)
    print("Total number of 8's:", b)
