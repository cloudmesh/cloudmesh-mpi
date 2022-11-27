import math
import multiprocessing
import numpy as np
from operator import truediv
from generate import Generator

# binary search
def b_search(arr, val, ineq):
    # "<": find largest value in arr that is less than val
    # ">": find smalles value in arr that is greater than val
    if ineq == "<":
        # to keep splits the same, we can reverse the array
        # otherwise, for "<" and ">" of the same value, 
        # we would need to keep and discard opposite halves of arrays
        arr = np.flip(arr)
    l = 0 # left pointer
    r = len(arr) - 1 # right pointer

    while (l < r):
        mid = (l + r) // 2 # find midpoint between l and r
        # check if middle element fulfills given inequality
        to_check = str(arr[mid]) + ineq + str(val)
        # print(f"to check: {to_check}")
        if eval(to_check): 
            # lower half
            r = mid
        else:
            # upper half
            l = mid + 1

    if ineq == "<":
        # reverse flip done above
        arr = np.flip(arr)
        return len(arr) - l - 1
    else:
        return l

# given two sorted arrays, merge them
def adaptive_merge(left, right):
    left = np.array(left)
    right = np.array(right)
    if Generator().verify(">", left):
        # reverse array
        left = np.flip(left)
    if Generator().verify(">", right):
        right = np.flip(right)

    # order arrays based on minimum
    # we always want left to have a smaller minimum than right
    l_min = left[0] # smallest element of left
    r_min = right[0]
    if (r_min < l_min):
        tmp = left
        left = right
        right = tmp
        # redefine because of swap
        l_min = left[0]
        r_min = right[0]

    l_max = left[len(left) - 1] # largest element of left
    r_max = right[len(right) - 1]

    # left and right separate, have no overlap
    if l_max <= r_min:
        # visual representation of left and right
        # ----
        #         ----
        # simply concatenate and return
        return np.concatenate((left, right))
    
    # left and right overlap, but not completely
    elif l_max > r_min and l_max < r_max:
        # visual representation
        # ---------
        #      ----------
        # we want to find and isolate the overlap
        # -----|----
        #      -----|-----

        # search for the smallest element in left that is larger than r_min
        l_idx = b_search(left, r_min, ">")
        # search for the largest element in right that is smaller than l_max
        r_idx = b_search(right, l_max, "<")
        
        # this part of left is already sorted and can be separated
        left_sorted = left[:l_idx]
        # similarly, also sorted
        right_sorted = right[r_idx + 1:]

        # isolate and merge middle part from left and right
        unsorted = np.concatenate((left[l_idx:], right[:r_idx+1]))
        unsorted = np.array(sorted(unsorted))

        return np.concatenate((left_sorted, unsorted, right_sorted))

    # left entirely contains right
    elif l_max >= r_max:
        # visual representation
        # ----------
        #   ----
        # break left into three parts, like so
        #--|----|----
        #   ----

        # find smallest element in left that is larger than r_min
        l_idx_min = b_search(left, r_min, ">")
        # find largest element in left that is smaller than r_max
        l_idx_max = b_search(left, r_max, "<")

        # isolate sorted, separate ends
        left_sorted_min = left[:l_idx_min]
        left_sorted_max = left[l_idx_max + 1:]

        # merge middle part of left with all of right, and sort
        unsorted = np.concatenate((right, left[l_idx_min:l_idx_max + 1]))
        unsorted = np.array(sorted(unsorted))
        
        return np.concatenate((left_sorted_min, unsorted, left_sorted_max))

