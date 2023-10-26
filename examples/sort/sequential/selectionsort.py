"""Selection sort."""


def selectionsort(order, arr):
    """
    Sorts the given array with type defined at creation time with
    a selection sort algorithm.

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

    if order in ["<"]:
        for i in range(n):
            # find min element in unsorted array
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            # place min element at end of sorted array
            (arr[i], arr[min_idx]) = (arr[min_idx], arr[i])
    else:
        for i in range(n):
            # find min element in unsorted array
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] > arr[min_idx]:
                    min_idx = j
            # place min element at end of sorted array
            (arr[i], arr[min_idx]) = (arr[min_idx], arr[i])
