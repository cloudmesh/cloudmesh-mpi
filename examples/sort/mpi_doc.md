# MPI (Message Passing Interface) Mergesort

This project implements an MPI mergesort algorithm. 

Packages used: Numpy, Pandas, Seaborn, Matplot

## Source Code

The source code is located in GitHub at the following location:

* <https://github.com/cloudmesh/cloudmesh-mpi/tree/main/examples/sort>

We distinguish the following important files:

* [sandra.ipynb](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/sandra.ipynb)
  

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



## Overview

This project uses Python to implement a multiprocessing mergesort algorithm (linked [here](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/multiprocessing_mergesort.py)). The algorithm is then run and evaluated in [sandra.ipynb](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/sandra.ipynb). 

### Mergesort

The unsorted array is generated on rank 0. Since the unsorted array must be split into smaller subarrays, _sub_size_ is calculated. _sub_size_ is the size of each subarray. It is equal to the size of the unsorted array divided by the number of processors, since each processor must be sent a subarry. Note that _n_, the size of the unsorted array, must be evenly divisible by the total number of processors. 

Once the subarrays have been distributed using the Scatter command, they are sorted on each processor using the built-in NumPy sort. This sort defaults to quicksort. 



