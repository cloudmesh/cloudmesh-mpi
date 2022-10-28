# Multiprocessing Mergesort

This project implements a multiprocessing mergesort algorithm. It then analyzes the algorithm using 
factors like input size, number of processors, speedup, and efficiency.

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

### Running the Algorithm

Running of the algorithm is controlled by [run.py](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/run.py). This can be run using the command
```bash
$ ./run.py --user=[user name] --node=[node name for stopwatch] --sort=[sort algorithm]
```

An example command:
```bash
$ ./run.py  --size=10000000 --repeat=1 --user=gregor --node=5950x
```

This would run the multiprocessing mergesort algorithm on arrays of size 10000000 for the user gregor. run.py will automatically calculate the number of processors _n_ for the user and run _repeat_ times using each number 1 to _$n_ of processors. 

In the example above, _repeat = 1_, so the algorithm will run only once on for each number of processors from 1 to _n_. Note that the algorithm will run a total of _n x repeat_ times. 

run.py runs the mergesort to generate data, which is collected using StopWatch. This data is stored in a specified log file named after the user. 

### Analyzing the Data

Analysis of the algorithm is controlled by [sandra.ipynb](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/sandra.ipynb). Functions _read_log_ and _get_average_ are imported from [analysis.py](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/analysis.py). These functions are used to streamline the outputted data and collect the relevant information from each line of data. 

The function _plot_benchmark_by_size_ plots a specified benchmark by each possible number of processers for a constant size of array to be sorted for each user on the same graph. 

Note that for maximum accuracy, each run can be repeated multiple times and the results can be averaged to prevent luck from skewing the experimental times. 

#### Calculating Speedup

One important function is _calculate_speedup_. Speedup is defined as _T(1) / T(n)_, where _T(1)_ is the time the algorithm takes on just one processor, and _T(n)_ is the time taken using _n_ processors. 

### Calculating Efficiency

Another important function is _calculate_efficiency_. Effiency is defined as _S(n) / n_, where _S(n)_ is the speedup of _n_. 

## Benchmark

![multiprocessing mergesort size = 10000000](images/by-size-10000000-multiprocessing_mergesort-alex-gregor.png)

**Figure 1:** Multiprocessing Mergesort size = 10000000

In Figure 1 we show the graph with efficiency as y-axis and number of processors as x-axis for sets of size 10000000 for users alex (blue) and gregor (orange). One can see that efficiency for alex continously decreases as the number of processors increases, while the efficiency for gregor increases slightly near the beginning and then decreases. 


## Old Notes

1. install

    - do once

    - create virtual anvironment

   ```bash
   pip install pip -U
   pip install -r requirements.txt
   ```


## List of sort algorithms in python

* [array.sort](https://docs.python.org/3/howto/sorting.html)
* [numpy.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html)

## Other sort algorithms

* [Counting Sort](https://en.wikipedia.org/wiki/Counting_sort)
* [Adaptive merge sort](https://www.tutorialspoint.com/adaptive-merging-and-sorting-in-data-structure)
* [Adaptive sort](https://en.wikipedia.org/wiki/Adaptive_sort)

## Speeding up the sequential algorithms

```python
from numba import jit

@jit
def sort_alg(a)
	# do sorting of a
	return a
```
