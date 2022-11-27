# quicksort
# https://www.geeksforgeeks.org/python-program-for-quicksort/

# THis version is not properly implemented

# partition array into two sections
from numba import jit


@jit
def split(arr, l, r):
    i = l + 1
    j = r
    k = arr[l]  # partition variable

    while True:
        # find j to the right of k and less than k
        while i <= j and arr[j] >= k:
            j -= 1
        # find i to the left of k and greater than k
        while i <= j and arr[i] <= k:
            i += 1
        # swap so both are in correct location
        if (i <= j):
            (arr[i], arr[j]) = (arr[j], arr[i])
        else:
            break
    # arr[l] = k, must be put into proper position
    (arr[l], arr[j]) = (arr[j], arr[l])
    return j


@jit
def quicksort(order, a, l=None, r=None):
    """
    order is ignored for now

    :param order:
    :type order:
    :param arr:
    :type arr:
    :param l:
    :type l:
    :param r:
    :type r:
    :return:
    :rtype:
    """
    raise NotImplementedError
    if l is None:
        l = 0
    if r is None:
        r = len(a) - 1
    if l >= r:
        return
    k = split(a, l, r)
    # don't include k, since it's already sorted
    quicksort("<", a, l, k - 1)
    quicksort("<", a, k + 1, r)
