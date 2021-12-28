## Parallel Sorting in Python with MPI

One can start just with the sequential algorithms first.

### Merge Sort

#### Sequential

#### Multiprocessing

(lower priority)

#### Parallel 

MPI

### Insertion  Sort

#### Sequential

#### Multiprocessing

(lower priority)

#### Parallel

MPI

### Insertion  Sort

#### Sequential

#### Multiprocessing

(lower priority)

#### Parallel

MPI

### Heap Sort

#### Sequential

#### Multiprocessing

(lower priority)

#### Parallel

MPI

### Quick Sort

#### Sequential

#### Multiprocessing

(lower priority)

#### Parallel

MPI

### MPI Search Combinations

A combination is a cobination of multiple sort algorithms that use dependent on the size on a node a variety of algorithms.
Let us assume te number of processors is p and the total number of elements is n. Thus there are n/p elements on each node. Let k <= n/p that defines the number of items that are either sorted sequentially or with a multithreaded algorithm. 
Let t denote the number of threads.

We investigate here suitable combinations in which the sorting is performed. We denote the combination of algorithms with 

A = (MPI sort, p, Node sort, t, k)

Thus 

A = (mergesort, 8, mergesort, 1, n/p) 

denotes a mergesort that is done in parallel on all nodes as well as combining the nodes.

A = (mergesort, 8, quicksort, 1, n/p)  where n/p > 4000

denotes that a parallel merge sort is run on all 8 processors. However, in the node itself on the lowest level we run a quicksort on all n/p elements.

### Benchmark

Use the cloudmesh StopWatch to conduct the benchmark. This will also print the details of the machine and allows reproducability on othe machines. 
We will write a shell script that runs the baenchmark with a variety of combinations, so we can reproduce it on other peoples machines.


#### Sequential


#### Parallel


#### Combined

Lets find some combinations and try them out to see what performs bets

#### Properties of lists

* random
* presorted
* sequential with n number of random swaps
* reverse order

How is the the sort strategy effected by perturbation from a sequential list




