# Multiprocessing Mergesort

Put intro here.
- what
- how

## Source Code

The source code is located in GitHub at the following location:

* <https://github.com/cloudmesh/cloudmesh-mpi/tree/main/examples/sort>

We distinguish the following important files:

* [sandra.ipynb](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/sandra.ipynb)
* 
## Installation

- how to install
- ENV3
- MPI directory cloning & compiling
- verify correctness
  
### ENV3

- Mac 
```bash
python -m venv ~/ENV3
source ~/ENV3/bin/activate
```

### Clone

To download our code, please follow the instructions:

```bash
mkdir cm
cd cm
git clone git@github.com:cloudmesh/cloudmesh-mpi.git
```


## Benchmark

- created using program ...
- recreate using ...

![multiprocessing mergesort size = 10000000](images/by-size-10000000-multiprocessing_mergesort-alex-gregor.png)

**Figure 1:** Multiprocessing Mergesort size = 10000000

In Figure 1 we show...


## Old Notes

## Gregors new experiment.py

Example:

```bash
./experiment.py --processes="[1-5,8]" --size="[100]" --repeat=10 
```

Help:

```bash
./experiment.py --help 
```

Bug:

At this time the log file parameter is not implemented. We may remove it.

## Simple use of git

0. download
    - do once

   ```bash
   mkdir cm
   cd cm
   git clone git@github.com:cloudmesh/cloudmesh-mpi.git
   ```

1. update

   ```bash
   git pull
   ```

2. local upload


1. to add file, do once

   ```bash
   git add filename
   ```

2. once changed file, do

   ```bash
   git commit -m "this is my comment" filename
   ```

3. remote upload

   ```bash
   git push
   ```

3. verify

   go to the web page and look att the file you modified

4. install

    - do once

    - create virtual anvironment

   ```bash
   pip install pip -U
   pip install -r requirements.txt
   ```

Never modify anythin in docs, Only Gregor does this!!!

## List of sort algorithms in python

* [array.sort](https://docs.python.org/3/howto/sorting.html)
*

[numpy.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html)

## Other sort algorithms

* [Countung Sort](https://en.wikipedia.org/wiki/Counting_sort)
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

## User Manual