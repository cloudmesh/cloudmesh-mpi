from mpi4py import MPI

# Communicator
comm = MPI.COMM_WORLD

# Number of processes in the communicator group
size = comm.Get_size()

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()

# Each process gets different data, depending on its rank number
data = (rank+1)**2

# Print data in each process
print("before gathering, data on rank %d is "%comm.rank, data)

# Gathering occurs
data = comm.gather(data, root=0)

# Process 0 prints out the gathered data, rest of the processes
# print their data as well
if rank == 0:
    print("after gathering, process 0's data is ", data)
else:
    print("after gathering, data in rank %d is "%comm.rank, data)
