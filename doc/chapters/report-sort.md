# MPI Mergesort

This project implements an MPI (Message Passing Interface) mergesort
algorithm.

Packages used: Numpy, Pandas, Seaborn, Matplot

## Source Code

The source code is located in GitHub at the following location:

* <https://github.com/cloudmesh/cloudmesh-mpi/tree/main/examples/sort>

We distinguish the following important files:

* [night.py](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/night.py)
  

## Installation

### ENV3 

TODO

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

Go to the [Github](https://github.com/cloudmesh/cloudmesh-mpi) to
verify that the correct repository has been cloned.

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
./mpi_run.py --user={username} --node={node} --sort={mpi_mergesort}--size={size} --repeat={repeat} --id={id}
```

Please read the Input section for specific documentation on each
option.


## Overview

This project uses Python to implement an MPI mergesort algorithm
(linked
[here](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/night.py)). The
algorithm is then run and evaluated in
[mpi_run.py](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/mpi_run.py).

### Input

* _mpi_run.py_ has several inputs.

* _user_: specify the username of whoever is running the program

* _node_: name of computer node on which program is being run

* _sort_: type of sort that is being run. Use "mpi_mergesort".

* _size_: size of array to sort

* _repeat_: number of times to run sorting algorithm. The final time
  will be the average of all runs.

* _id_: specifies the merging algorithm that is used to merge the
  arrays once they've been sent from one process to another, also
  known as the merge algorithm. Each id number corresponds to a
  specific algorithm.

  * 0: built-in Python _sorted_
  * 1: sequential merge
  * 2: adaptive merge

For example, if John would like to run the MPI mergesort on his
Raspberry Pi 4, and he would like to use an array of size 200,
repeating 10 times, and use an adaptive merge to combine the the
arrays between processes, he would use the command

```bash
./mpi_run.py --user=john --node=pi4 --sort=mpi_mergesort --size=200 --repeat=10 --id=2
```


### Mergesort

The unsorted array is generated on rank 0. Since the unsorted array
must be split into smaller subarrays, _sub_size_ is
calculated. _sub_size_ is the size of each subarray. It is equal to
the size of the unsorted array divided by the number of processors,
since each processor must be sent a subarry. Note that _n_, the size
of the unsorted array, must be evenly divisible by the total number of
processors.

Once the subarrays have been distributed using the Scatter command,
they are sorted on each processor using the built-in Python. This sort
defaults to Timsort.

In order to merge the sorted subarrays, we can visualize the
processors as being set up in a binary tree, where each parent has two
children. One important note: in this situation, the left child also
functions as the parent node. We can then split the tree into two
sections: left children and right children. Because we are using a
binary tree, we know that the number of left and right children will
always be equal. Therefore, we can create a variable _split_ that
splits the set of processors in half.

If the rank of the processor is in the second half (between _split_
and _split_ * 2), then it will send its sorted subarray to its "left"
partner to be merged. Otherwise, if the rank of the processor is in
the first half (between 0 and _split_), it will recieve a sorted
subarray from its "right" partner and then merge it with the subarray
that it currently contains. When a subarray is sent, it is sent to the
processor with rank _rank - split_, ensuring that the processor that
it is sent to has a rank between 0 and _split_. This guarantees that
each subarray that is sent gets sent to a merging
processor. Similarly, when a subarray is received, it is received from
a processor with rank _rank + split_, ensuring that the subarray is a
sorted array to be merged. This mapping guarantees a unique pairing
between left and right child.

Once received, the subarrays are merged together. The merging
algorithm can be defined by the user, and will be referred to as the
**merge algorithm**. There are currently three merging algorithms that
can be used.

1. **sequential_merge_fast**, a "fast" merge that simply combines the
   two arrays using the built-in Python _sorted_ function. Note that
   sorting algorithms can also be used to merge.

2. **sequential_merge_python**, a merge that uses the well-known
   technique of appending the smaller of two array elements to a third
   array

3. **adaptive_merge**, a custom sort algorithm that takes advantage of
   pre-existing order in the sequence. It is described in more detail
   <a name="adaptive">[here](#adaptive)</a>

Then, each individual send/recieve operates as following:

1. Left child sends sorted subarray

2. Right child allocates memory for recieving subarray from left child
   (_local_tmp_)

3. Right child allocates memory for array to store merged result
   (_local_result_)

4. Right child receives subarray

5. Right child merges received subarray with its own subarray

6. Right child assigns _local_arr_ to point to _local_result_

This loop continues until the tree reaches the height that guarantees
us a single sorted list. Each time, the number of nodes is halved
(since two have been merged into one).

### Output

The output of the program is generated and logged in
[mpi_experiment.py](hhttps://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/mpi_experiment.py). This
file runs the sort according to user specifications. Three of the most
important things it does:

1. The specific algorithm is run _repeat_ times. Note that the larger
   _repeat_ is, the more accurate the final mean time will be. The
   mean time is not calculated here. Rather, all times from each
   repeat will be outputted.

2. Maps id numbers to merge types. It's important to be able to
   differentiate between data outputted by each merge type, since we'd
   like to examine the differences. However, we'd also like to keep
   the titles/inputs concise, which is why id numbers are used. Each
   id number is translated to its merge type in the program.

3. Times the runs. Running the sort is done by a bash command, so by
   starting a timer, running the command, and stopping the timer, we
   can get the full amount of time it took to run the sort. This is a
   more accurate measure than placing timers inside of the actual sort
   program (night.py), since it is able to time the MPI
   initialization, which timers inside the program wouldn't be able to
   do.

### Final Run Method

This is the outermost run program, i.e. the one that a user will
run. See the above Input section for an example of how to run
this. [mpi_run.py](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/mpi_run.py)
generates a log file and runs
[mpi_experiment.py](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/mpi_experiment.py).

## Adaptive TBD

This sort takes advantage of pre-existing sorted subsequences in two
arrays to merge them together. It is designed to merge two sorted
arrays together. Given two arrays, called _left_ and _right_, we first
calculate the min and max values in both.

```python
   l_min = left[0] 
   r_min = right[0]
   l_max = left[len(left) - 1]
   r_max = right[len(right) - 1]
```

We can also assume that the minimum of left will always be smaller
than the minimum of right (if not, we can just swap them).

The sort splits into three scenarios based on `l_min`, `r_min`,
`l_max`, and `r_max`:

### No overlap

This would be if `l_max <= r_min`. 
In this case, a visual representation of the arrays could look like this.

```bash
left
------------
                  ----------
                     right
```

where the arrays are entirely disjoint. Then, we can just concatenate
the two and return.

### Some overlap

This would be if _l_max_ were between _r_min_ and _r_max_, or 
_l_max_ > _r_min_ and _l_max_ < _r_max_. 

A visual representation: 

```bash
left
--------------
         -----------------
                     right
```

Then, we want to split both arrays into two parts:

```bash
left
---------|-----
          -----|------------
                     right
```

If we take the divider in _left_ and call it _l_idx_, we can see that
everything to the left of _l_idx_ is completely separate from _right_
with no overlap. Similarly, everything to the right of the divider in
_right_ has no overlap with any of _left_.

Then, how do we define these dividers? Note that the visual is
slightly misleading: the arrays are not continuous spans of numbers,
rather, they are individual scattered points that span from a min to a
max. Then, if we want to find _l_idx_ such that everything to the left
of _l_idx_ doesn't overlap with _right_, we want to find the index of
the smallest element in _left_ that is greater than _r_min_. Since
every element to the left would then be less than or equal to _r_min_,
that point would then be the _l_idx_ we are looking for.

Similarly, we want to search in _right_ for some _r_idx_ where
everything to the right of _r_idx_ has no overlap with _left_. Then,
we want to find the index of the largest element in _right_ that is
less than _l_max_. Since every element to the right would then be
greater or equal to _l_max_, that point would be _r_idx_.

From here, binary search is employed to find such points. Read the
Binary search section for more information.

Once _l_idx_ and _r_idx_ are found, we can then separate out the
disjoint parts.

```python
left_sorted = left[:l_idx]
right_sorted = right[r_idx + 1:]
```

The remaining parts can then be concatenated and sorted. This sort uses the Python builtin sort. 
```python
unsorted = np.concatenate((left[l_idx:], right[:r_idx+1]))
unsorted = np.array(sorted(unsorted))
```

Finally, the left sorted portion, the now-sorted middle portion, and
the right sorted portion are concatenated and returned.

### Complete overlap

This would be if _l_max_ >= _r_max_.

A visual representation:

```bash
left
-------------------
      ------
      right
```

Then, we want to split _left_ into three parts:

```bash
left
------|------|-------
       ------
      right
```

Let the leftmost divider in _left_ be _left_sorted_min_, and the
rightmost divider in _left_ be _left_sorted_max._ Then, everything to
the left of _left_sorted_min_ has no overlap with _right_, and
everything to the right of _left_sorted_max_ has no overlap with
_right_.

To find _left_sorted_min_, we want to find the smallest element in
_left_ that is larger than _r_min_. To find _left_sorted_max_, we want
to find the largest element in _left_ that is smaller that _r_max_. We
can do this using binary search - the specific algorithm is described
in the Binary search section.

We can isolate the sorted, separate ends with

```python
left_sorted_min = left[:l_idx_min]
left_sorted_max = left[l_idx_max + 1:]
```

Then, we can merge the middle of _left_ and all of _right_ together
and sort the resulting array using the builtin Python sorted.

```python
unsorted = np.concatenate((right, left[l_idx_min:l_idx_max + 1]))
unsorted = np.array(sorted(unsorted))
```

Finally, the left end, the sorted middle section, and the right end
can be concatenated together and returned.

### Binary search

This binary search takes in three parameters:

1. _arr_: the array in which to search
2. _val_: the value with which to compare, and
3. _ineq_: the comparision with which to compare the result to val

Expressed in words:

If _ineq_ = "<", we are searching for the largest value in _arr_ that is less than _val_.

If _ineq_ = ">", we are searching for the smallest value in _arr_ that is greater than _val_. 

The actual algorithm is classic. Calculate a middle value and perform
a boolean-evaluating statement. If true, take the lower half of the
array. Otherwise, take the upper half of the array. However, note that
if the array is increasing, this will only work if _ineq_ = ">", since
true will always lead to the upper half of the array.

Instead of writing two different binary searches, we make two crucial
changes to the function:

1. **Using eval statements.** Instead of hardcoding a < or a > in the if-statement, we can instead construct a statement to check. 

   ```python
   to_check = str(arr[mid]) + ineq + str(val)
   eval(to_check)
   ```

   Doing this allows us to have both "<" and ">" statements, depending on
   which one is inputted.

2. **Reversing the array.** If the _ineq_ = "<" and the array is
   increasing, this function will never work, since we always take the
   upper half of the array when the check statement is true. However,
   if the array is decreasing, then taking the upper half works: those
   values are the ones that are less than _val_, and the ones we want
   to continue to search in. At the end, we can reverse the array, and
   flip the answer to the reversed index, i.e. 2 would become the 2nd
   index from the end.

   ```python
   arr = np.flip(arr)
   return len(arr) - l - 1
   ```

## Analyzing the Results

Analysis of the data takes place in
[mpi.ipynb](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/mpi.ipynb).

The function _get_data_ extracts data from the logfiles. It
specifically gets the number of processes, the time, the size of the
array, the id, and name, and the tag from each line of output in each
log file. This data is then formatted using Pandas DataFrames.

We can then plot the data using _plot_benchmark_by_size_. This
function generates the name, title, and graphs the given data by
whichever specific attribute the user would like.

![Performance comparision of different sorting Algorithms](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/chapters/images/mpi-mpi_mergesort-0-1-2.png){ width=50% }

The above figure shows the relationship between increasing size of
array and time of sorting for three different merging
algorithms. Recall that 0 is the Python builtin sort, 1 is the
iterative merge, and 2 is the adaptive sort. The sizes of the arrays
used are [100, 1000, 10000, 100000, 1000000, 5000000, 7000000,
10000000]. We can see that for the first half of sizes, all three
sorts appear to perform roughly the same. However, once we pass that
point, the builtin Python sort performs much better than the other
two. We can also see that while the adaptive merge always performs
better than the iterative merge, it is still slower than the builtin
Python sort. Lastly, we can observe the very low variability of the
Python builtin sort, even as array size increases. Both the other two
sorts have a great deal of variation, but the builtin sort stays
relatively precise.