# TODO: docstrings are missing

def listsort(order, arr):
    """
    Sorts the given array with type defined at creation time with
    a build in  .sort() function.

    :param order: the order in which to sort. It has the value "<" for
                  ascending and ">" for descending.
    :type order: str
    :param arr: The array to be sorted. This can be a numerical array
                including int or float
    :type arr: defined when the array is created.
    :return: sorted array
    :rtype: the type of the original array
    """
    if order in ["ascending", "<"]:
        return arr.sort()
    elif order in ["descending", ">"]:
        return arr.sort(reverse=True)

def listsorted(order, arr):
    """
    Sorts the given array with type defined at creation time with
    the build in sorted()function.

    :param order: the order in which to sort. It has the value "<" for
                  ascending and ">" for descending.
    :type order: str
    :param arr: The array to be sorted. This can be a numerical array
                including int or float
    :type arr: defined when the array is created.
    :return: sorted array
    :rtype: the type of the original array
    """
    # less efficient than slistsort
    if order in ["ascending", "<"]:
        return sorted(arr)
    elif order in ["descending", ">"]:
        return sorted(arr, reverse=True)
