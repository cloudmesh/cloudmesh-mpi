import mpi4py

def merge_sort(array, comm, sort_function=None, order="<"):
  # Get the number of processes.
  num_processes = comm.Get_size()

  # If there is only one process, sort the array sequentially.
  if num_processes == 1:
    return sorted(array)

  # Split the array into equal-sized chunks.
  chunk_size = len(array) // num_processes
  chunks = [array[i:i + chunk_size] for i in range(0, len(array), chunk_size)]

  # Sort each chunk in parallel.
  for i in range(num_processes):
    comm.send(chunks[i], dest=i)

  # Merge the sorted chunks together.
  sorted_array = []
  for i in range(0, num_processes, 2):
    if i + 1 < num_processes:
      sorted_array.append(merge(chunks[i], chunks[i + 1]))
    else:
      sorted_array.append(chunks[i])

  # Return the sorted array.
  return sorted_array

def merge(array1, array2):
  # Initialize the output array.
  output_array = []

  # Iterate over the two arrays, merging the elements together.
  i = 0
  j = 0
  while i < len(array1) and j < len(array2):
    if array1[i] <= array2[j]:
      output_array.append(array1[i])
      i += 1
    else:
      output_array.append(array2[j])
      j += 1

  # Append the remaining elements of the first array.
  while i < len(array1):
    output_array.append(array1[i])
    i += 1

  # Append the remaining elements of the second array.
  while j < len(array2):
    output_array.append(array2[j])
    j += 1

  # Return the merged sorted array.
  return output_array
