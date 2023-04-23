import mpi4py

def mergesort(array):
  """Sorts an array in parallel using MPI4py.

  Args:
    array: The array to sort.

  Returns:
    A sorted array.
  """

  # Get the number of processes.
  comm = mpi4py.MPI.COMM_WORLD
  size = comm.Get_size()

  # Check if the number of processes is a power of 2.
  if size & (size - 1):
    raise ValueError("The number of processes must be a power of 2.")

  # Split the array into equal chunks.
  chunk_size = len(array) // size
  chunks = [array[i * chunk_size:(i + 1) * chunk_size] for i in range(size)]

  # Sort each chunk in parallel.
  for i in range(size):
    comm.Bcast(chunks[i], root=0)
    mpi4py.util.quicksort(chunks[i])

  # Merge the sorted chunks.
  sorted_array = []
  for i in range(0, len(array), chunk_size):
    start = i
    end = min(i + chunk_size, len(array))
    sorted_array.extend(mpi4py.util.merge(chunks[start // chunk_size], chunks[(start + 1) // chunk_size], start, end))

  return sorted_array
