#!/usr/bin/env python
import random
import sys
import time
from contextlib import contextmanager
from multiprocessing import Manager, Pool

def merge_sort_multiple(results, array):
  results.append(merge_sort(array))


def merge_multiple(results, array_part_left, array_part_right):
  results.append(merge(array_part_left, array_part_right))


def merge_sort(array):
    array_length = len(array)

    if array_length <= 1:
        return array

    middle_index = int(array_length / 2)
    left = array[0:middle_index]
    right = array[middle_index:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    sorted_list = []
    # We create shallow copies so that we do not mutate
    # the original objects.
    left = left[:]
    right = right[:]
    # We do not have to actually inspect the length,
    # as empty lists truth value evaluates to False.
    # This is for algorithm demonstration purposes.
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        elif len(left) > 0:
            sorted_list.append(left.pop(0))
        elif len(right) > 0:
            sorted_list.append(right.pop(0))
    return sorted_list


@contextmanager
def process_pool(size):
    """Create a process pool and block until
    all processes have completed.
    Note: see also concurrent.futures.ProcessPoolExecutor"""
    pool = Pool(size)
    yield pool
    pool.close()
    pool.join()


def parallel_merge_sort(array, process_count):

    # Divide the list in chunks
    step = int(len(array) / process_count)

    # Instantiate a multiprocessing.Manager object to
    # store the output of each process.
    # See example here
    # http://docs.python.org/library/multiprocessing.html#sharing-state-between-processes
    manager = Manager()
    results = manager.list()

    with process_pool(size=process_count) as pool:
        for n in range(process_count):
            # We create a new Process object and assign the
            # merge_sort_multiple function to it,
            # using as input a sublist
            if n < process_count - 1:
                chunk = array[(n * step):((n + 1) * step)]
            else:
                # Get the remaining elements in the list
                chunk = array[n * step:]
            pool.apply_async(merge_sort_multiple, (results, chunk))


    print('Performing final merge.')


    # For a core count greater than 2, we can use multiprocessing
    # again to merge sub-lists in parallel.
    while len(results) > 1:
        print(94)
        with process_pool(size=process_count) as pool:
            pool.apply_async(
                merge_multiple,
                (results, results.pop(0), results.pop(0))
            )

    final_sorted_list = results[0]


if __name__ == '__main__':
    length = 1000000
    unsorted = [random.randint(0, n * 100) for n in range(length)]
    parallel_merge_sort(unsorted, 4)