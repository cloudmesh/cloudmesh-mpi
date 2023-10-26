""" insertion sort."""


# TODO: docstrings are missing
def insertionsort(order, arr):
    """

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
        for i in range(1, n):
            x = arr[i]
            j = i - 1
            # shift all elements greater than x to the right by 1
            while j >= 0 and x < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            # insert x
            arr[j + 1] = x
    elif order in ["descending", ">"]:
        for i in range(1, n):
            x = arr[i]
            j = i - 1
            # shift all elements less than x to the right by 1
            while j >= 0 and x > arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            # insert x
            arr[j + 1] = x
    return arr
