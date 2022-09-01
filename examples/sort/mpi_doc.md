# MPI (Message Passing Interface) Mergesort

This project implements an MPI mergesort algorithm. 

Packages used: Numpy, Pandas, Seaborn, Matplot

## Source Code

The source code is located in GitHub at the following location:

* <https://github.com/cloudmesh/cloudmesh-mpi/tree/main/examples/sort>

We distinguish the following important files:

* [night.py](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/night.py)
  

## Installation

### ENV3 (for macOS)
```bash
$ python -m venv ~/ENV3
$ source ~/ENV3/bin/activate
```

### Clone

To download our code, please follow the instructions:

```bash
$ mkdir cm
$ cd cm
$ git clone git@github.com:cloudmesh/cloudmesh-mpi.git
```

### Verification

Go to the [Github](https://github.com/cloudmesh/cloudmesh-mpi) to verify that the correct repository has been cloned. 

### Updating

1. Update local version

   ```bash
   git pull
   ```

2. To add file (only do once)

   ```bash
   git add filename
   ```

3. Once file is changed, do

   ```bash
   git commit -m "this is my comment" filename
   ```

4. Remote upload

   ```bash
   git push
   ```

## Running the Program

Run the program using the command

   ```bash
   ./mpi_run.py --user={username} --node={node} --sort={mpi_mergesort }--size={size} --repeat={repeat} --id={id}
   ```

   Please read the Input section for specific documentation on each option.


## Overview

This project uses Python to implement an MPI mergesort algorithm (linked [here](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/night.py)). The algorithm is then run and evaluated in [mpi_run.py](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/mpi_run.py). 

### Input

_mpi_run.py_ has several inputs.

_user_: specify the username of whoever is running the program\
_node_: name of computer node on which program is being run\
_sort_: type of sort that is being run. Use "mpi_mergesort".\
_size_: size of array to sort\
_repeat_: number of times to run sorting algorithm. 
Final time will be the average of all runs.\
_id_: specifies which sorting algorithm to use on each process.\
0: built-in Python _sorted_\
1: sequential merge\
2: adaptive merge


### Mergesort

The unsorted array is generated on rank 0. Since the unsorted array must be split into smaller subarrays, _sub_size_ is calculated. _sub_size_ is the size of each subarray. It is equal to the size of the unsorted array divided by the number of processors, since each processor must be sent a subarry. Note that _n_, the size of the unsorted array, must be evenly divisible by the total number of processors. 

Once the subarrays have been distributed using the Scatter command, they are sorted on each processor using the built-in NumPy sort. This sort defaults to quicksort. 

In order to merge the sorted subarrays, we can visualize the processors as being set up in a binary tree, where each parent has two children. One important note: in this situation, the left child also functions as the parent node. We can then split the tree into two sections: left children and right children. Because we are using a binary tree, we know that the number of left and right children will always be equal. Therefore, we can create a variable _split_ that splits the set of processors in half. 

If the rank of the processor is in the second half (between _split_ and _split_ * 2), then it will send its sorted subarray to its "left" partner to be merged. Otherwise, if the rank of the processor is in the first half (between 0 and _split_), it will recieve a sorted subarray from its "right" partner and then merge it with the subarray that it currently contains. When a subarray is sent, it is sent to the processor with rank _rank - split_, ensuring that the processor that it is sent to has a rank between 0 and _split_. This guarantees that each subarray that is sent gets sent to a merging processor. Similarly, when a subarray is received, it is received from a processor with rank _rank + split_, ensuring that the subarray is a sorted array to be merged. This mapping guarantees a unique pairing between left and right child. 

Once received, the subarrays are merged together. The merging algorithm can be defined by the user. There are currently two merging algorithms that can be used: a sequential merge that uses the well-known technique of using appending the smaller of two array elements to a third array, or a "fast" merge that simply combines the two arrays using the built-in Python _sorted_ function. 

Then, each individual send/recieve operates as following:

1. Left child sends sorted subarray
2. Right child allocates memory for recieving subarray from left child (_local_tmp_)
3. Right child allocates memory for array to store merged result (_local_result_)
4. Right child receives subarray
5. Right child merges received subarray with its own subarray
6. Right child assigns _local_arr_ to point to _local_result_

This loop continues until the tree reaches the height that guarantees us a single sorted list. Each time, the number of nodes is halved (since two have been merged into one). 