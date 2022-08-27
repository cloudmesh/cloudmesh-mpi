# inspired by https://devopslog.wordpress.com/2012/04/15/mergesort-example-using-python-multiprocessing/
# and https://gist.github.com/stephenmcd/39ded69946155930c347
import math
import multiprocessing
import numpy as np
from operator import truediv
from generate import Generator


def b_search(arr, val, ineq):
    if ineq == "<":
        arr = np.flip(arr)
    l = 0
    r = len(arr) - 1

    while (l < r):
        mid = (l + r) // 2
        to_check = str(arr[mid]) + ineq + str(val)
        # print(f"to check: {to_check}")
        if eval(to_check): 
            r = mid
        else:
            l = mid + 1
    if ineq == "<":
        arr = np.flip(arr)
        return len(arr) - l - 1
    else:
        return l

def adaptive_merge(left, right):
    left = np.array(left)
    right = np.array(right)
    if Generator().verify(">", left):
        # reverse array
        left = np.flip(left)
    if Generator().verify(">", right):
        right = np.flip(right)

    # order arrays
    l_min = left[0]
    r_min = right[0]
    if (r_min < l_min):
        tmp = left
        left = right
        right = tmp
        # redefine because of swap
        l_min = left[0]
        r_min = right[0]

    l_max = left[len(left) - 1]
    r_max = right[len(right) - 1]

    # left and right separate
    if l_max <= r_min:
        # print("OPTION 1")
        # ----
        #       ----
        return np.concatenate((left, right))
    elif l_max > r_min and l_max < r_max:
        # print("OPTION 2")
        # -------
        #    -------
        l_idx = b_search(left, r_min, ">")
        r_idx = b_search(right, l_max, "<")

        left_sorted = left[:l_idx]
        # print(f"left sorted: {left_sorted}")
        right_sorted = right[r_idx + 1:]
        # print(f"right sorted: {right_sorted}")
        unsorted = np.concatenate((left[l_idx:], right[:r_idx+1]))
        unsorted = np.array(sorted(unsorted))
        return np.concatenate((left_sorted, unsorted, right_sorted))
    elif l_max >= r_max:
        # print("OPTION 3")
        # -------
        #   ---  
        l_idx_min = b_search(left, r_min, ">")
        l_idx_max = b_search(left, r_max, "<")
        left_sorted_min = left[:l_idx_min]
        left_sorted_max = left[l_idx_max + 1:]
        unsorted = np.concatenate((right, left[l_idx_min:l_idx_max + 1]))
        unsorted = np.array(sorted(unsorted))
        return np.concatenate((left_sorted_min, unsorted, left_sorted_max))

