import math


# heap sort

# using binary tree
# left child of node i = 2i + 1
# right child of node i = 2i + 2
# parent of node i = (i - 1) / 2


def max_heapify(arr, n, i):
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
