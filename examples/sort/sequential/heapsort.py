import math

# TODO: docstrings are missing

# heap sort

# using binary tree
# left child of node i = 2i + 1
# right child of node i = 2i + 2
# parent of node i = (i - 1) / 2


def max_heapify(arr, n, i):
    """

    :param arr:
    :type arr:
    :param n:
    :type n:
    :param i:
    :type i:
    :return:
    :rtype:
    """
    big = i
    # node i's two children
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[big]:
        big = l
    if r < n and arr[r] > arr[big]:
        big = r

    # if l or r greater than i, swap
    if big != i:
        (arr[i], arr[big]) = (arr[big], arr[i])
        # heapify again on new i
        max_heapify(arr, n, big)


# build min heap
def min_heapify(arr, n, i):
    """

    :param arr:
    :type arr:
    :param n:
    :type n:
    :param i:
    :type i:
    :return:
    :rtype:
    """
    m = i
    # node i's two children
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] < arr[m]:
        m = l
    if r < n and arr[r] < arr[m]:
        m = r

    # if l or r greater than i, swap
    if m != i:
        (arr[i], arr[m]) = (arr[m], arr[i])
        # heapify again on new i
        min_heapify(arr, n, m)


def heapsort(order, arr):
    """
    Sorts the given array with type defined at creation time with
    a heap sort algorithm.

    :param order: the order in which to sort. It has the value "<" for
                  ascending and ">" for descending.
    :type order: str
    :param arr: The array to be sorted. This can be a numerical array
                including int or float
    :type arr: defined when the array is created.
    :return: sorted array
    :rtype: the type of the original array
    """
    n = len(arr)
    if order in ["ascending", "<"]:
        # build max heap from bottom up
        for i in range(math.ceil(n / 2), -1, -1):
            max_heapify(arr, n, i)

        # swap and heapify
        for i in range(n - 1, 0, -1):
            # swap max of current heap to position i and remove from heap
            (arr[i], arr[0]) = (arr[0], arr[i])
            max_heapify(arr, i, 0)

    elif order in ["descending", ">"]:
        # build min heap from bottom up
        for i in range(math.ceil(n / 2), -1, -1):
            min_heapify(arr, n, i)

        # swap and heapify
        for i in range(n - 1, 0, -1):
            # swap max of current heap to position i and remove from heap
            (arr[i], arr[0]) = (arr[0], arr[i])
            min_heapify(arr, i, 0)
