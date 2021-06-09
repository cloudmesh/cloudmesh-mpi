from mpi4py import MPI

# Communicator
comm = MPI.COMM_WORLD

# Number of processes in the communicator group
size = comm.Get_size()

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()

# Process with rank 0 gets a list with the data to be scattered
if rank == 0:
    data = [(i+1)**2 for i in range(size)]
else:
    data = None

# Print data in each process
print("before scattering, data on rank %d is "%comm.rank, data)

# Scattering occurs
data = comm.scatter(data, root=0)

# Print data in each process after scattering
print("data for rank %d is "%comm.rank, data)
