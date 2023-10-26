# bubble sort
# https://www.geeksforgeeks.org/python-program-for-bubble-sort/

# TODO: docstrings are missing

def bubblesort(order, arr):
    """
    Sorts the given array with type defined at creation time with
    a bubblesort algorithm.

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
        for i in range(n - 1):
            for j in range(n - i - 1):
                # swap unordered pairs
                if arr[j] > arr[j + 1]:
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
    elif order in ["descending", ">"]:
        for i in range(n - 1):
            for j in range(n - i - 1):
                # swap unordered pairs
                if arr[j] < arr[j + 1]:
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
